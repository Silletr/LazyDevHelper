import base64
import configparser
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from contextlib import suppress
from pathlib import Path

from platformdirs import user_cache_path


config = None


def is_virtual() -> bool:
    return is_virtual_env() or is_conda()


def is_virtual_env() -> bool:
    # The check for sys.real_prefix covers virtualenv, the equality of
    # non-empty sys.base_prefix with sys.prefix covers venv.
    # note: Python versions before 3.3 don't have sys.base_prefix
    # if you're not in virtual environment
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def get_config() -> dict:
    dconf = {}
    if is_virtual_env() is False:
        dconf = _conda_cfg()
    else:
        prefix = _get_prefix()
        _read_config(os.path.join(prefix, "pyvenv.cfg"))

        dconf = dict(config["root"])
        dconf["prefix"] = prefix

    return dconf


def _conda_cfg() -> dict:
    data = {}

    data["home"] = os.path.join(os.environ["CONDA_PREFIX"], "bin")
    data["prefix"] = _get_prefix()
    data["include-system-site-packages"] = False
    data["prompt"] = os.environ["CONDA_DEFAULT_ENV"]

    path = os.path.join(os.environ["CONDA_PREFIX"], "conda-meta", "python*")

    files = glob.glob(path)
    if len(files) > 0:
        with open(files[0], "r") as fp:
            conda_info = json.load(fp)

    data["version"] = conda_info["version"]

    return data


def is_venv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(os.path.join(prefix, "pyvenv.cfg"))

    if is_virtualenv() is False:
        return True
    else:
        return False


def is_virtualenv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(os.path.join(prefix, "pyvenv.cfg"))

    if "virtualenv" in config["root"]:
        return True
    else:
        return False

def is_uv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(os.path.join(prefix, "pyvenv.cfg"))

    if "uv" in config["root"]:
        return True
    else:
        return False


def is_conda() -> bool:
    is_conda = False
    try:
        os.environ["CONDA_DEFAULT_ENV"]
        is_conda = True
    except Exception:
        pass
    try:
        os.environ["CONDA_PREFIX"]
        is_conda = True
    except Exception:
        pass

    return is_conda


def running_from_activated_env() -> bool:
    running = False
    try:
        os.environ["VIRTUAL_ENV"]
        running = True
    except Exception:
        pass

    return running


def _get_prefix() -> str:
    return sys.real_prefix if hasattr(sys, "real_prefix") else sys.prefix


def _read_config(path: str) -> None:
    global config
    if config is None:
        conf = configparser.ConfigParser()
        with open(path) as stream:
            # Add fake section name to make pyvenv.cfg compatible with ConfigParser
            conf.read_string("[root]\n" + stream.read())
        config = conf


def _read_config_static(path: str) -> dict:
    config = {}
    conf = configparser.ConfigParser()
    with open(path) as stream:
        # Add fake section name to make pyvenv.cfg compatible with ConfigParser
        conf.read_string("[root]\n" + stream.read())
    config = dict(conf["root"])
    return config


def check_dir(path: str | Path) -> dict:
    if isinstance(path, str) is True:
        path = Path(path)

    if path == Path("."):
        path = Path(os.getcwd())

    config = {}
    # Check classic virtual env in a given directory
    for file in path.iterdir():
        if file.is_dir() is True:
            # include/ dir is not checked because PDM, Hatch and uv are not creating it by default
            if (
                (file / "bin").exists() is True
                and (file / "bin" / "activate").exists() is True
                and (file / "lib").exists() is True
                and (file / "pyvenv.cfg").exists() is True
            ):
                config = _read_config_static(str(file / "pyvenv.cfg"))
                config["path"] = str(file)
                if "virtualenv" in config.keys():
                    config["source"] = "virtualenv"
                elif "uv" in config.keys():
                    config["source"] = "uv"
                else:
                    config["source"] = "venv"

    # Check for poetry
    poetry_hash = generate_env_name(path.name, str(path))
    # From https://github.com/python-poetry/poetry/blob/108d7323280889b277751807fb7d564674fe6896/src/poetry/locations.py
    poetry_root = Path(user_cache_path("pypoetry", appauthor=False))

    poetry_venvs = poetry_root / "virtualenvs"
    poetry_envs = list(Path(poetry_venvs).glob(f"{poetry_hash}-*"))
    if poetry_venvs.exists() is True and len(poetry_envs) > 0:
        config = _read_config_static(str(poetry_envs[0] / "pyvenv.cfg"))
        config["path"] = str(poetry_envs[0])
        config["source"] = "poetry"

    # Check for pipenv
    pipenv_hash = generate_env_name(path.name, str(path / "Pipfile"))
    pipenv_root = Path("~/.local/share").expanduser() / "virtualenvs"

    if pipenv_root.exists() is True and (pipenv_files := Path(pipenv_root).glob("*")):
        for pipenv_file in pipenv_files:
            if pipenv_file.name == pipenv_hash:
                config = _read_config_static(str(pipenv_file / "pyvenv.cfg"))
                config["path"] = str(pipenv_file)
                config["source"] = "pipenv"

    return config


def scan_dir(path: str) -> list[str]:
    output = subprocess.check_output(
        f"find {path} -name activate -type f 2>/dev/null", shell=True
    )
    envs = output.decode("utf-8")
    validated_envs = []
    for line in envs.split("\n"):
        if len(line) > 0:
            cpath = Path(line)
            # include/ dir is not checked because PDM, Hatch and uv are not creating it by default
            if (
                (cpath.parent.parent / "bin").exists() is True
                and (cpath.parent.parent / "lib").exists() is True
                and (cpath.parent.parent / "pyvenv.cfg").exists() is True
            ):
                validated_envs.append(cpath.parent.parent)
    return validated_envs


def _encode(string: str, encodings: list[str] | None = None) -> bytes:
    if isinstance(string, bytes):
        return string
    encodings = encodings or ["utf-8", "latin1", "ascii"]
    for encoding in encodings:
        with suppress(UnicodeEncodeError, UnicodeDecodeError):
            return string.encode(encoding)
    return string.encode(encodings[0], errors="ignore")


# Poetry and Pipenv have different functions but they work exactly the same.
# The only difference is that pipenv is hashing the path to the Pipfile file
# while Poetry is hashing only the directory path. Here is the Poetry's implementation
# but it is used for both Poetry and Pipenv.
# From https://github.com/python-poetry/poetry/blob/108d7323280889b277751807fb7d564674fe6896/src/poetry/utils/env/env_manager.py#L751-L759
# For Pipenv implementation please look here:
# https://github.com/pypa/pipenv/blob/951c382cfd066c6cf014e5c18049bd9259456c24/pipenv/project.py#L536
def generate_env_name(name: str, cwd: str) -> str:
    name = name.lower()
    sanitized_name = re.sub(r'[ $`!*@"\\\r\n\t]', "_", name)[:42]
    normalized_cwd = os.path.normcase(os.path.realpath(cwd))
    h_bytes = hashlib.sha256(_encode(normalized_cwd)).digest()
    h_str = base64.urlsafe_b64encode(h_bytes).decode()[:8]
    return f"{sanitized_name}-{h_str}"

import subprocess
import sys

print(">> python/pip_install.py imported")


def install_lib(lib_name: str):
    print(f"📦 Installing {lib_name} ...")
    try:
        result = subprocess.run(
            ["pip3", "install", lib_name, "--upgrade"],
            capture_output=False,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(result.stdout)

        if result.stderr:
            print(result.stderr)
            with open("requirements.txt", "a") as file:
                file.write(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {lib_name}")
        print(e.stderr)


def main():
    if len(sys.argv) < 2:
        print("⚠️ Provide at least one lib")
        return

    for lib in sys.argv[1:]:
        install_lib(lib)


if __name__ == "__main__":
    main()

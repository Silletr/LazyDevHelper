<<<<<<< HEAD
#!/usr/bin/env python3

print(">>> pip_install started <<<")
>>>>>>> main
import subprocess
import sys

print(">> python/pip_install.py imported")


def install_lib(lib_name: str):
    print(f"📦 Installing {lib_name} ...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", lib_name, "--break-system-packages"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        output = result.stdout.lower()
        
        if "requirement already satisfied" in output:
            print(f"✅ {lib_name} already installed")
        elif "successfully installed" in output:
            print(f"✅ {lib_name} successfully installed")
            with open("requirements.txt", "a")
        else:
            print(f"Installation result:\n{output.splitlines()[0]}")
       print(result.stdout)

        if result.stderr:
            print(result.stderr)
            with open("requirements.txt", "a") as file:
                file.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {lib_name}")
        print(e.output)


def main():
    if len(sys.argv) < 2:
        print("⚠️ Provide at least one lib")
        return

    for lib in sys.argv[1:]:
        install_lib(lib)


if __name__ == "__main__":
    main()

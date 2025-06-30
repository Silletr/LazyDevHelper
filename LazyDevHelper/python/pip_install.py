#!/usr/bin/env python3

print(">>> pip_install started <<<")
import subprocess
import sys


def install_lib(lib_name: str):
    print(f"📦 Installing {lib_name} ...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", lib_name, "--break-system-packages"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        print(f"Installing {lib_name} on processing\n")
        output = result.stdout.lower()
        
        if "requirement already satisfied" in output:
            print(f"✅ {lib_name} already installed")
        elif "successfully installed" in output:
            print(f"✅ {lib_name} successfully installed")
        else:
            print(f"Installation result:\n{output.splitlines()[0]}")
        
        with open("requirements.txt", "a") as file:
            file.write(f"{lib_name}\n")

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

#!/usr/bin/env python3
print(">>> pip_install started <<<")

import subprocess
import sys

def install_lib(lib_name: str):
    print(f"📦 Installing {lib_name} ...\n")
    try:
        global result
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", lib_name, "--break-system-packages"],
            check=True,
            text=True,
            capture_output=True, 
        )
        
       
        if "requirement already satisfied" in result.stdout.lower():
            print("\nInstallation Output:")
            print(result.stdout)
            print(f"✅ {lib_name} already installed")
        elif "successfully installed" in result.stdout.lower():
            print(f"✅ {lib_name} successfully installed")
           
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {lib_name}")
        print(e.output)


def main():
    if len(sys.argv) < 2:
        print("Provide at least one lib")
        return

    for lib in sys.argv[1:]:
        install_lib(lib)


if __name__ == "__main__":
    main()

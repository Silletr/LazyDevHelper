import subprocess
from python.pip_check import get_installed_libs

def install_lib():
    installed_libs = get_installed_libs()
    if installed_libs:
        print(f"Found {len(installed_libs)} installed packages:")
        for lib in installed_libs:
            print(f"- {lib}")
    else:
        print("No packages found")


if __name__ == "__main__":
    install_lib()

import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print()
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}\n"
              "Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n")

        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n")

        print("Then run this program again.")
    else:
        print()
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment:", os.environ.get("VIRTUAL_ENV_PROMPT"))
        print("Environment Path:", os.environ.get("VIRTUAL_ENV"))

        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n")

        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")

import sys


def print_file() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], "r")
    except FileNotFoundError as error:
        print(f"Error opening file {sys.argv[1]}: {error}")
    except PermissionError as error:
        print(f"Error opening file {sys.argv[1]}: {error}")
    else:
        print("---\n")
        r_file = file.read()
        print(r_file)
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    write_file()

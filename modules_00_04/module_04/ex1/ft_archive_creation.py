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
        print(f"File '{sys.argv[1]}' closed.\n")
        write_file()


def write_file() -> None:
    print("Transform data:")
    print("---\n")

    file = open(sys.argv[1], "r")
    r_file = file.read()

    lines = r_file.splitlines()
    updated_lines = "".join([f"{line}#\n" for line in lines])

    print(updated_lines)
    file_to_save = input("Enter new file name (or empty): ")
    if file_to_save:
        file_to_write = open(file_to_save, "w")
        file_to_write.write(updated_lines)
        print(f"Saving data to '{file_to_save}\n"
              f"Data saved in file '{file_to_save}'.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    print_file()

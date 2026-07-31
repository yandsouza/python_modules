def secure_archive(file: str, mode: str, opt_w: str = "") -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(file, mode, encoding="utf-8") as f:
                r_file = f.read()
        if mode == "w":
            with open(file, mode, encoding="utf-8") as f:
                f.write(opt_w)
    except FileNotFoundError as error:
        return (False, f"{error}")
    except PermissionError as error:
        return (False, f"{error}")
    else:
        if mode == "r":
            return (True, r_file)
        else:
            return (True, "Content successfully written to file")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("master.passwd", "r"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print()

    print("Using 'secure_archive' to write previous content to a new file: ")
    print(secure_archive("ancient_fragment.txt", "w", "New text"))
    print()

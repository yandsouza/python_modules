import sys


def ft_command_quest() -> None:
    i = 1
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        while i < len(sys.argv):
            print(f"Arguments {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()

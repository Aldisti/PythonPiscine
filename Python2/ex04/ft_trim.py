
from sys import argv

def trim(chars: list) -> None:
    chars.pop(0)
    chars.pop(-1)
    return

def main() -> None:
    if len(argv) < 3:
        print("Error! You must insert at least 2 values")
        return
    chars = list(argv[1:])
    trim(chars)
    print(f"The new list is: {chars}")

if __name__ == '__main__':
    main()


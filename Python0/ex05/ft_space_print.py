
def main() -> None:
    s = input("Insert a string: ")
    l = len(s)
    if l < 20:
        print(" " * (20 - l) + s)
    else:
        print(s[(l - 20):])

if __name__ == '__main__':
    main()

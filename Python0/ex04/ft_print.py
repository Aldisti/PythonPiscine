
def main() -> None:
    s = input("Insert a string: ")
    i = int(input("Insert an integer: "))
    if (i > len(s)):
        print("Error: index out of range")
    else:
        print(s[i:-i + 1])

if __name__ == '__main__':
    main()

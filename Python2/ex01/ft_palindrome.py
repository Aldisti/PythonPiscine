
from sys import argv

def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "")
    return s[:(len(s) // 2)] == s[-(len(s) // 2):][::-1]

def main() -> None:
    if len(argv) != 2:
        print("Error! Insert just 1 string!")
        return
    if is_palindrome(argv[1]):
        print(f"The string {argv[1]} is palindrome")
    else:
        print(f"The string {argv[1]} is not palindrome")
    

if __name__ == '__main__':
    main()


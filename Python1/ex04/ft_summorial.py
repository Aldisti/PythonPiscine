
from sys import argv

def main() -> None:
    if len(argv) != 2:
        print("Error! Usage: python3 ft_summorial.py <n>")
        return
    elif int(argv[1]) < 0:
        print("Error! n must be >=0")
        return
    i = 0
    n = int(argv[1])
    while i < int(argv[1]):
        n += i
        i += 1
    print("The sum is:", n)

if __name__ == '__main__':
    main()


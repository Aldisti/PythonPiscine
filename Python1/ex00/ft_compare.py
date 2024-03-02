
from sys import argv

def main() -> None:
    n1 = float(argv[1])
    n2 = float(argv[2])
    if n1 > n2:
        print(f"{n1} is greater than {n2}")
    elif n1 == n2:
        print(f"{n1} is equal to {n2}")
    else:
        print(f"{n1} is less than {n2}")

if __name__ == '__main__':
    main()



from sys import argv

def main() -> None:
    if len(argv) != 4:
        print("Error! Usage: python3 ft_min.py <x> <y> <z>")
        return
    n = float(argv[1])
    for i in argv[2:]:
        if float(i) < n:
            n = float(i)
    print("The min is:", n)
    

if __name__ == '__main__':
    main()

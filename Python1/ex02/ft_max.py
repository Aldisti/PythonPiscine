
from sys import argv

def main() -> None:
    if len(argv) != 4:
        print("Error! Usage: python3 ft_max.py <x> <y> <z>")
        return
    n = float(argv[1])
    for i in argv[2:]:
        if float(i) > n:
            n = float(i)
    print("The max is:", n)
    

if __name__ == '__main__':
    main()

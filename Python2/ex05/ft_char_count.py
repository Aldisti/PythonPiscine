
from sys import argv

def main() -> None:
    if len(argv) < 2:
        print("Error! No string given")
        return
    chars = dict()
    for av in argv[1:]:
        for c in av.lower():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    print("Char count:")
    for i in sorted(chars):
        print(f"{i} = {chars[i]}")

if __name__ == '__main__':
    main()


def get_num(type: str, value: int=1) -> int:
    return int(input("Insert " + type + ": ")) * value

def main() -> None:
    print("Result:", get_num("hours", 3600) + get_num("minutes", 60) + get_num("seconds"))

if __name__ == '__main__':
    main()


def main() -> None:
    exps = input("Insert an expression: ")
    res = eval(exps)
    if res < 0:
        res = -res
    print("Result:", res)

if __name__ == '__main__':
    main()



def sum_list(nums: list) -> int:
    n = 0
    for i in nums:
        n += i
    return n

def main() -> None:
    nums = []
    while True:
        nums.append(int(input("Insert integer: ")))
        if nums[-1] == 0:
            break
    print("The sum is:", sum_list(nums))

if __name__ == '__main__':
    main()

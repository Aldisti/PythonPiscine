
from sys import argv

def main() -> None:
    if len(argv) < 3:
        print("Error! You must insert at least 2 numbers")
        return
    is_ordered: bool = True
    tmp: int = int(argv[1])
    nums = []
    for i in argv[1:]:
        nums.append(int(i))
        if int(i) <= tmp: tmp = int(i)
        else: is_ordered = False
    if is_ordered:
        print("The inserted sequence is sorted!")
    else:
    	print(f"The correct order is {sorted(nums, reverse=True)}")

if __name__ == '__main__':
    main()


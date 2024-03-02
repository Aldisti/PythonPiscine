
from sys import argv

def main() -> None:
    size = len(argv) - 1
    if size < 1:
        print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
        return
    nums = [int(i) for i in argv[1:]]
    nim = (nums[0], 0)
    nax = (nums[0], 0)
    i = 1
    while i < size:
        if nim[0] > nums[i]: nim = (nums[i], i)
        if nax[0] < nums[i]: nax = (nums[i], i)
        i += 1
    print(
		f"The min is {nim[0]} and its position is: {nim[1]}",
        f"The max is {nax[0]} and its position is: {nax[1]}",
        sep='\n'
	)

if __name__ == '__main__':
    main()


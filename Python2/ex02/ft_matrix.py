
from sys import argv

def main() -> None:
    if len(argv) != 3:
        print("Error! Usage: python3 ft_matrix.py <n> <m>")
        return
    n = float(argv[1])
    m = float(argv[2])
    sum_rows = []
    sum_cols = []
    mat = []
    for x in range(int(n)):
        mat.append([])
        sum_rows.append(0)
        for y in range(int(m)):
            sum_cols.append(0)
            mat[x].append(float(input(f"Insert the element in position ({x}, {y}): ")))
            sum_rows[x] += mat[x][y]
            sum_cols[y] += mat[x][y]
    print("The inserted matrix is:")
    for i in mat: print(i)
    print("The sum over rows is:")
    print(sum_rows)
    print("The sum over columns is:")
    print(sum_cols[:int(m)])

if __name__ == '__main__':
    main()




FILE_PATH = "./words.txt"

def insert_sorted(tab: list[str], word: str) -> None:
    if len(tab) == 0:
        tab.append(word)
        return
    i = 0
    for w in tab.copy():
        if w > word:
            tab.insert(i, word)
            return
        i += 1
    tab.append(word)

def main() -> None:
    read_file = input("Insert file name: ")
    try:
        file = open(read_file, 'r')
    except:
        print("Error! The specified file does not exist!")
        return
    n = int(input('Insert an integer: '))
    words = []
    while True:
        word = file.readline()
        if word == "":
            break
        word = word.strip('\n')
        if len(word) <= n:
            continue
        insert_sorted(words, word)
    file.close()
    print(f"The words longer than {n} are the following:")
    for word in words:
        print(word)

if __name__ == '__main__':
    main()


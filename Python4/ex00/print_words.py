
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
    n = int(input('Insert an integer: '))
    words = []
    with open(FILE_PATH, 'r') as file:
        while True:
            word = file.readline()
            if word == "":
                break
            word = word.strip('\n')
            if len(word) <= n:
                continue
            insert_sorted(words, word)
    print(f"The words longer than {n} are the following:")
    for word in words:
        print(word)

if __name__ == '__main__':
    main()


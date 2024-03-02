
READ_FILE = "words.txt"
WRITE_FILE = "long_words.txt"

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
    with open(READ_FILE, 'r') as file:
        while True:
            word = file.readline()
            if word == "":
                break
            word = word.strip('\n')
            if len(word) <= n:
                continue
            insert_sorted(words, word)
    with open(WRITE_FILE, 'w') as file:
        for word in words:
            file.write(word + '\n')
    print(f"The words longer than {n} have been written on \"{WRITE_FILE}\"")

if __name__ == '__main__':
    main()


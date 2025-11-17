def get_num_words(book):
    words = book.split()
    num_words = len(words)
    return num_words


def get_char_count(book):
    char_count = {}
    letters = list(book.lower())
    for letter in letters:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count


def sort_on(items):
    return items["num"]


def sort_char_count(char_count):
    char_sort = []
    for c, n in char_count:
        char_sort.append({"char": c, "num": n})
    char_sort.sort(reverse=True, key=sort_on)
    return char_sort

from stats import get_num_words, get_char_count, sort_on, sort_char_count


def get_boot_text(book_path):
    with open(book_path) as b:
        return b.read()


def main():
    book = get_boot_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    char_sort = sort_char_count(char_count)
    print(f"Found {num_words} total words")
    print(char_sort)


main()

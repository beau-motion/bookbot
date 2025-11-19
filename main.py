import sys
from stats import get_num_words, get_char_count, sort_char_count


def get_boot_text(book_path):
    with open(book_path) as b:
        return b.read()


def list_char(char_sort):
    for item in char_sort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_boot_text(book_path)
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    char_sort = sort_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_char(char_sort)
    print("============= END ===============")


main()

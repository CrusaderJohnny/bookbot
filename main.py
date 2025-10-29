from stats import word_count, find_chars, sorting_hat
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    strings = get_book_text(file_path)
    count = word_count(strings)
    char_count = find_chars(strings)
    listed = sorting_hat(char_count)
    print_panel(file_path, count, listed)

def print_panel(file_path, count, listed):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in listed:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
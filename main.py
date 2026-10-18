import sys

from stats import character_count, chars_dict_to_sorted_list, word_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_Report(character_counts: list[tuple[str, int]]) -> None:
    for char, count in character_counts:
        if char.isalpha():
            print(f"{char}: {count}")


def main() -> None:
    print("======= Book BOT =======")
    if len(sys.argv) < 2:
        print("Please provide a path to a book file.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(f"Loaded book from {book_path} ...")
    character_counts = character_count(book_text)
    sorted_character_counts = chars_dict_to_sorted_list(character_counts)
    print('-------Word Count -------') 
    print(f"Found {word_count(book_text)} total words")
    print("-------- Character Count Report ------")
    print_Report(sorted_character_counts)

main()

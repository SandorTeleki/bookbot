import sys
from stats import words_in_book, number_of_characters, sorted_list_of_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def report(file_path, total_words, total_sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in total_sorted_characters:
        key = list(item.keys())[0]
        value = item[key]
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

def main ():
    file_path =  f"./{sys.argv[1]}"
    book_content = get_book_text(file_path)
    total_words = words_in_book(book_content)
    total_characters = number_of_characters(book_content)
    total_sorted_characters = sorted_list_of_characters(total_characters)

    report(file_path, total_words, total_sorted_characters)

main()

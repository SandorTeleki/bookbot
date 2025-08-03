from stats import words_in_book

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main ():
    file_path =  "./books/frankenstein.txt"
    # get_book_text(file_path)
    words_in_book(get_book_text(file_path))

main()

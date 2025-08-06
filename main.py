from stats import words_in_book, number_of_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main ():
    file_path =  "./books/frankenstein.txt"
    words_in_book(get_book_text(file_path))
    number_of_characters(get_book_text(file_path))
main()

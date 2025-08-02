def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def words_in_book(text):
    words = text.split()
    num_words = len(words)
    num_words 
    print(f"{num_words} words found in the document")

def main ():
    file_path =  "./books/frankenstein.txt"
    # get_book_text(file_path)
    words_in_book(get_book_text(file_path))

main()

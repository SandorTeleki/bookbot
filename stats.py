def words_in_book(text):
    words = text.split()
    num_words = len(words)
    num_words 
    print(f"{num_words} words found in the document")

def number_of_characters(text):
    letters = {}
    for letter in text:
        lowerCase = letter.lower()
        if lowerCase in letters:
            letters[lowerCase] += 1
        else:
            letters[lowerCase] = 1
    print(letters)
    return letters
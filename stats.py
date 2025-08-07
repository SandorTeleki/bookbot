def words_in_book(text):
    words = text.split()
    num_words = len(words)
    return num_words 

def number_of_characters(text):
    letters = {}
    for letter in text:
        lowerCase = letter.lower()
        if lowerCase in letters:
            letters[lowerCase] += 1
        else:
            letters[lowerCase] = 1
    return letters

def sorted_list_of_characters(letters):
    sorted_list = []
    for letter in letters:
        num = letters[letter]
        d = {"char": letter, "num": num}
        sorted_list.append(d)
    sorted_list.sort(reverse=True, key=sort_on)
    new_list = []
    for d in sorted_list:
        new_dict = {}
        new_dict[d["char"]] = d["num"]
        new_list.append(new_dict)
    return new_list

def sort_on(character):
    return character["num"]


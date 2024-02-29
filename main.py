def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_counted = letter_counter(text)
    print(f"{num_words} words found in the document")
    print(f"The following letters where counted {letters_counted}")

     



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def letter_counter(text):
    words = text.split()
    text = ''.join(words)
    lower_text = text.lower()
    letter_dict = {}

    for letter in lower_text:
        if letter in letter_dict: 
            letter_dict[letter] += 1
        else: 
            letter_dict[letter] = 1
    return letter_dict
        

main()
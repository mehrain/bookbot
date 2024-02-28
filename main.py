def main():
    word_count = 0
    with open("books/frankenstein.txt") as book:
        book_string = book.read()
        word_list = book_string.split()
        for i in range(0, len(word_list)):
            word_count += 1
    print(word_count)
        
        
main()
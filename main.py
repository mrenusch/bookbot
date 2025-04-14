
from stats import num_words
from stats import num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()




def main():
    # print(get_book_text('books/frankenstein.txt'))
    text = get_book_text('books/frankenstein.txt')

    print(num_words(text), "words found in the document")
    
    print(num_characters(text), "characters found in the document")

main()
    # print(get_book_text(books/frankenstein.txt
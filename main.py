


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def num_words(text):
    words = text.split()
    return len(words)

def main():
    # print(get_book_text('books/frankenstein.txt'))
    text = get_book_text('books/frankenstein.txt')

    print(num_words(text), "words found in the document")
    

main()
    # print(get_book_text(books/frankenstein.txt
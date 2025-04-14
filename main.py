
from stats import num_words
from stats import num_characters
from stats import sort_characters
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    

    text = get_book_text(sys.argv[1])

    print("Found", num_words(text), "total words")
    
    sorted_list = sort_characters(num_characters(text))
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
        else:
            # print(item["char"], ":", item["count"])
            pass
        # print(item["char"], ":", item["count"])
    # print(num_words(text), "words found in the document")
    # print(num_characters(text), "characters found in the document")
    
main()
    # print(get_book_text(books/frankenstein.txt
def num_words(text):
    words = text.split()
    return len(words)

def num_characters(text):
    char_counts = {}
    
    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char":char, "count":count})

    chars_list.sort(reverse=True, key=lambda x: x["count"])

    return chars_list
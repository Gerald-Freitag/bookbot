# stats.py

#opens and reads a text file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#counts the number of words from get_book_text  
def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

#consolidates the previous two functions and returns the word count
def get_num_words(filepath):
    return word_count(get_book_text(filepath))

# returns the number of letters in the text including spaces and symbols
def get_num_letters(text):
    letter_counts = {}
    text = text.lower()
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def get_letters(filepath):
    return get_num_letters(get_book_text(filepath))

def sorted_letters(char):
    return char['num']

# adds new identifiers to the dictionary and puts them in a list to be sorted.
def get_sorted_char_list(char_counts_dict):
    list_of_chars = []
    for char, count in char_counts_dict.items():
        new_dict = {}
        if char.isalpha():
            new_dict["char"] = char
            new_dict["num"] = count
            list_of_chars.append(new_dict)
    list_of_chars.sort(reverse=True, key=sorted_letters)
    return list_of_chars

def organized_list(filepath):
    return get_sorted_char_list(get_letters(filepath))
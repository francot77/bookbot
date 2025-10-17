from stats import get_num_words,count_chars
from sys import argv,exit
def get_book_text():
    if len(argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}")
    count_chars(get_num_words(argv[1]))
get_book_text()
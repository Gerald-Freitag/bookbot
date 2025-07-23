#main.py

from stats import get_num_words, get_letters, organized_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]} \n----------- Word Count ----------")
    
    result = get_num_words(sys.argv[1])
    print(f"Found {result} total words")
   
    print("--------- Character Count -------")

    final_list = organized_list(sys.argv[1])
    #print(final_list)

    for item in final_list:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()

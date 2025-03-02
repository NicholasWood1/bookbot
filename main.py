from stats import num_words_fn, count_chars , double_dict,sort_double_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


## Usage: python3 main.py <path_to_book>

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    #file_path = "./books/frankenstein.txt"
    book = get_book_text(sys.argv[1])
    
    num_words = num_words_fn(book)
    
    char_dict = count_chars(book)
    double = double_dict(char_dict)
    double.sort(reverse=True, key=sort_double_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    
    for i in range(0,len(double)):
        print(f"{double[i]["char"]}: {double[i]["count"]}")
    
    print("============= END ===============")

main()
from stats import get_num_words, get_character_count, sort_dict
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    filepath = sys.argv[1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
    book_content = get_book_text(filepath)

    word_count = get_num_words(book_content)
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    character_dict = get_character_count(book_content)
    print("--------- Character Count -------")
    sorted_dict = sort_dict(character_dict)
    for item in sorted_dict:
      print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()

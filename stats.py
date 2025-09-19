def get_num_words(book_content):
  split_content = book_content.split()
  return len(split_content)

def get_character_count(book_content):
  character_dict = {}

  for char in book_content:
    lower_char = char.lower()
    if lower_char in character_dict:
      character_dict[lower_char] += 1
    else:
      character_dict[lower_char] = 1

  return character_dict

def sort_on(items):
  return items["num"]

def sort_dict(dict):
  dict_in_list = []
  for key in dict:
    if key.isalpha():
      dict_in_list.append({
        "char": key,
        "num": dict[key]
      })

  dict_in_list.sort(reverse=True, key=sort_on)

  return dict_in_list

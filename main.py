def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    char_counts = character_count(file_contents)
    char_counts_list = dict_to_list(char_counts)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for item in char_counts_list:
      print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")

def character_count(string):
  lower_string = string.lower()
  dict = {}
  for char in lower_string:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  return dict

def dict_to_list(dict):
  items = []
  for key in dict:
    items.append({ "char": key, "count": dict[key] })
  return items

main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    converted_text = text.lower()
    letter_count_result = letter_count(converted_text)
    sorted_list = letters_dict_to_sorted_list(letter_count_result)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_list:
        print(f"The '{item['letter']}' letter was found {item['count']} times")

    print("--- End report ---")

    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def letter_count(converted_text):
    output = {}
    for letter in converted_text:
        if letter not in output:
            output[letter]= 1
        else:
            output[letter] += 1
    return output

def letters_dict_to_sorted_list(letter_count_result):
    sorted_letter_count = dict(sorted(letter_count_result.items()))
    sorted_list = []
    for letter in sorted_letter_count:
        if letter.isalpha() == True:
            sorted_list.append({"letter": letter, "count": sorted_letter_count[letter]})
    return sorted_list


        
main()
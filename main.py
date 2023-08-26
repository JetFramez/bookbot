def main():
    text = get_file_contents()
    words = num_words(text)
    charObj = character_count(text)
    fancy_print(charObj, words)


def sort_by_num(dic):
    arr = []
    for key in dic.keys():
        if key.isalpha():
            arr.append({'char': key, 'count': dic[key]})

    arr.sort(key=lambda x: x['count'], reverse=True)
    return arr


def fancy_print(dic, word_count):
    arr = sort_by_num(dic)
    print_arr = []
    print_arr.append("--- Begin report of books/frankenstein.txt ---")
    print_arr.append(f"{word_count} words found in the document")
    print_arr.append("")
    print_arr.append("")
    for item in arr:
        if item['char'].isalpha():
            print_arr.append(
                f"The '{item['char']}' character was found {item['count']} times")
    print_arr.append("")
    print_arr.append("")
    print_arr.append("--- End report ---")
    for item in print_arr:
        print(item)


def num_words(text):
    return len(text.split())


def get_file_contents():
    with open('books/frankenstein.txt') as f:
        return f.read()


def character_count(text):
    chars_dic = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars_dic:
            chars_dic[lower_char] += 1
        else:
            chars_dic[lower_char] = 1
    return chars_dic


main()

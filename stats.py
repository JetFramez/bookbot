def get_num_words(str):
    return len(str.split())

def get_chars_dict(str):
    dict = {}
    for char in str:
        key = char.lower()
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    return dict

def sort_on(item):
    return item["num"]

def get_sorted_chars(dict):
    sorted_list = []
    for char in dict:
        if char.isalpha():
            sorted_list.append({"char":char, "num":dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

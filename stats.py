def word_count(text):
    words = text.split()
    return len(words)

def find_chars(text):
    char_dic = {}
    for char in text.lower():
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

def sort_method(method):
    return method["num"]

def sorting_hat(dictionary):
    sorting_dic = []
    for item in dictionary:
        sorting_dic.append({"char": item, "num": dictionary[item]})
    sorting_dic.sort(reverse=True, key=sort_method)
    return sorting_dic
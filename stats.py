def num_words_fn(text):
    arr = text.split()
    return len(arr)


def count_chars(text):
    l_text = text.lower()
    char_counts = {}

    for char in l_text:   
        if char_counts.get(char) == None:
            char_counts[char] = 1

        else:
            char_counts[char] = char_counts[char] +1

    return char_counts

def double_dict(dict):
    # Double dict that has the char, num keys
    char_counts = {"char" : None, "count" : None}
    
    sorted_list_of_dicts = []
    
    for i in dict.keys(): 
        if i.isalpha() == True:
            char_counts["char"] = i
            char_counts["count"] = dict[i]
            sorted_list_of_dicts.append(char_counts)
            char_counts = {"char" : None, "count" : None}

    

    return sorted_list_of_dicts

def sort_double_dict(dict):
    return dict["count"]
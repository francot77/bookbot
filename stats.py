def get_num_words(filepath):
    with open(filepath) as f:
        file_content = f.read()
        words = file_content.split()
        num_words = len(words)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        return words

def count_chars(word_list:str):
    ndict = {}
    print("--------- Character Count -------")
    for word in word_list:
        for char in word:
            lowchar = char.lower()
            if lowchar in ndict:
                ndict[lowchar] +=1
            else:
                ndict[lowchar] = 1
    sorted_ndict = list(ndict.items())
    sorted_ndict.sort(key=lambda item: item[1],reverse=True)
    for key,value in sorted_ndict:
        print(f"{key}: {value}")
def repeated_word(string):
    hash = set()
    Mystring=string.replace(',', '')
    for word in Mystring.split():
        if word.lower() in hash:
            return word
        else:
            hash.add(word.lower())
    
    return 'None'





    
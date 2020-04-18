def text_analyzer(*s):
    """
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    """
    lower = 0
    upper = 0
    space = 0
    punc = 0
    i = 0
    if not s:
        s = input("What is the text to analyse?\n>>")
    while i < len(s):
        if s[i].islower():
            lower += 1
        elif s[i].isupper():
            upper += 1
        elif s[i].isspace():
            space += 1
        elif not s[i].isalpha():
            punc += 1
        i += 1
    print ("The text contains", i, " characters:\n")
    print ('- ', upper, ' upper letters\n')
    print ('- ', lower, ' lower letters\n')
    print ('- ', punc,'punctuation marks\n')
    print ('- ', space, ' spaces')
    return
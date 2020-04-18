def text_analyzer(s):
    upper = 0
    lower = 0
    punc = 0
    space = 0
    char = 0
    for i in s:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
        elif i.isspace():
            space = space + 1
        elif not i.isdigit():
            punc = punc + 1
        char = char + 1
    print("The text contains ", char, " characters:\n")
    print("- ", upper, " upper letters\n")
    print("- ", lower, " lower letters\n")
    print("- ", punc, " punctuation marks\n")
    print("- ", space, " spaces")
    return
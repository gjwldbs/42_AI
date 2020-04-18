import sys
def stringtomorse(s):
    morse = ""
    s = " ".join(s)
    for i in s:
        if i == ' ' or i == '/':
            morse += i
        elif i == 'A' or i == 'a':
            morse += ".-"
        elif i == 'B' or i == 'b':
            morse += "-..."
        elif i == 'C' or i == 'c':
            morse += "-.-."
        elif i == 'D' or i == 'd':
            morse += "-.."
        elif i == 'E' or i == 'e':
            morse += "."
        elif i == 'F' or i == 'f':
            morse += "..-."
        elif i == 'G' or i == 'g':
            morse += "--."
        elif i == 'H' or i == 'h':
            morse += "...."
        elif i == 'I' or i == 'i':
            morse += ".."
        elif i == 'J' or i == 'j':
            morse += ".---"
        elif i == 'K' or i == 'k':
            morse += "-.-"
        elif i == 'L' or i == 'l':
            morse += ".-.."
        elif i == 'M' or i == 'm':
            morse += "--"
        elif i == 'N' or i == 'n':
            morse += "-."
        elif i == 'O' or i == 'o':
            morse += "---"
        elif i == 'P' or i == 'p':
            morse += ".--."
        elif i == 'Q' or i == 'q':
            morse += "--.-"
        elif i == 'R' or i == 'r':
            morse += ".-."
        elif i == 'S' or i == 's':
            morse += "..."
        elif i == 'T' or i == 't':
            morse += "-"
        elif i == 'U' or i == 'u':
            morse += "..-"
        elif i == 'V' or i == 'v':
            morse += "...-"
        elif i == 'W' or i == 'w':
            morse += ".--"
        elif i == 'X' or i == 'x':
            morse += "-..-"
        elif i == 'Y' or i == 'y':
            morse += "-.--"
        elif i == 'Z' or i == 'z':
            morse += "--.."
        elif i == '0':
            morse += '-----'
        elif i == '1':
            morse += '.----'
        elif i == '2':
            morse += '..---'
        elif i == '3':
            morse += '...--'
        elif i == '4':
            morse += '....-'
        elif i == '5':
            morse += '.....'
        elif i == '6':
            morse += '-....'
        elif i == '7':
            morse += '--...'
        elif i == '8':
            morse += '---..'
        elif i == '9':
            morse += '----.'
        else:
            morse = 'ERROR'
    print(morse)

length = len(sys.argv)
if length > 1:
    lst = sys. argv[1].split()
    i = 2
    while i < length:
        lst.extend(sys.argv[i].split())
        i += 1
    error = 0
    check_s = ''.join(lst)
    for j in check_s:
        if j == '/':
            error = 1
    if error == 0:
        s = "/".join(lst)
        stringtomorse(s)
    else:
        print("ERROR")
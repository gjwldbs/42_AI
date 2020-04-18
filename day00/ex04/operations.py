import sys

if len(sys.argv) > 3 or not (sys.argv[1]).isdigit() or not (sys.argv[2]).isdigit():
    if len(sys.argv) > 3:
        print("InputError: too many arguments\n")
    elif not (sys.argv[1]).isdigit() or not (sys.argv[2]).isdigit():
        print("InputError: only numbers\n")
    print("Usage: python operations.py <number 1> <number 2>")
    print("Example:\n   python operations.py 10 3\n>")
elif len(sys.argv) == 3:
    sum = int(sys.argv[1]) + int(sys.argv[2])
    print("Sum:         ", sum)
    dif = int(sys.argv[1]) - int(sys.argv[2])
    print("Difference:  ", dif)
    mul = int(sys.argv[1]) * int(sys.argv[2])
    print("Product:     ", mul)
    if not int(sys.argv[2]) == 0:
        div = float(sys.argv[1]) / float(sys.argv[2])
        print("Quotient:    ", div)
        rem = int(sys.argv[1]) % int(sys.argv[2])
        print("Remainder:   ", rem)
    elif int(sys.argv[2]) == 0:
        print("ERROR (div by zero)")
        print("ERROR (modulo by zero)")
    print(">")
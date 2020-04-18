import sys

s = sys.argv[1]
i = 2
while i < len(sys.argv) :
    s = s + " " + sys.argv[i]
    i = i + 1
print (s.swapcase()[::-1])
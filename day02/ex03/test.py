fp = open('good.csv', 'r')

txt = fp.read()
lst = txt.split('\n')
skip_top = 0
skip_bottom = 18
sep = ','
lst = lst[skip_top: (len(lst) - skip_bottom)]
print(lst[1:])
txt = "\n".join(lst)
print(txt)
#print("hi")
lst = txt.replace('\n', ',').split(',')
print(lst)

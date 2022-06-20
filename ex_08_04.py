fname = input("Enter:")
opfile = open(fname)
rdfile = opfile.read()
orglst = rdfile.split()
orglst.sort()
lst = list()
#print(orglst)
for word in orglst:
    if word not in lst:
        lst.append(word)
print(lst)

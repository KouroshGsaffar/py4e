fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File can not be opened:', fname)
    quit()
stuff=list()
for line in fh:
    line=line.rstrip()
    words= line.split()
    for i in words:
        if not i in stuff:
            stuff.append(i)
        else: continue
stuff.sort()
print(stuff)

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File can not be opened:', fname)
    quit()
for line in fh:
    fw=line.rstrip()
    print(fw.upper())

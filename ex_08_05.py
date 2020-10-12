fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File can not be opened:', fname)
    quit()
count=0
stuff=list()
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):continue
    if not line.startswith('From'): continue
    count=count+1
    words= line.split()
    print(words[1])
print('There were', count, 'lines in the file with From as the first word')

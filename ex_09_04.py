name= input('Enter file:')
try:
    fh=open(name)
except:
    print('File can not be opened:', name)
    quit()
counts=dict()
for line in fh:
    if line.startswith('From:'): continue
    if not line.startswith('From'): continue
    words=line.split()
    counts[words[1]]=counts.get(words[1],0)+1
bigcount=None
bigname=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount=count
        bigname=word
print(bigname,bigcount)

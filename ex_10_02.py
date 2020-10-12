name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print('The file could not open:', name)
    quit()
counts=dict()
for line in handle:
    if line.startswith('From:'): continue
    if not line.startswith('From'): continue
    line=line.rstrip()
    words=line.split()
    time=words[5]
    time=time.split(':')
    counts[time[0]]=counts.get(time[0],0)+1
for k,v in sorted(counts.items()):
    print(k,v)

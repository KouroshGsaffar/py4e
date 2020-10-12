fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File can not be opened:', fname)
    quit()
count=0
total=0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count=count+1
    index=line.find('0')
    number=float(line[index:])
    total=total+number
average=float(total/count)
print('Average spam confidence:', average)

import re
hand=open('regex_sum_296007.txt')
# hand=open('regex_sum_42.txt')
numlist=list()
for line in hand:
    y= re.findall('[0-9]+',line)
    if len(y) <0 :  continue
    for num in y:
        number=float(num)
        numlist.append(number)
print('Sum:', int(sum(numlist)))

text = "X-DSPAM-Confidence:    0.8475"
index=text.find('0')
number=text[index:]
number=float(number)
print(number)

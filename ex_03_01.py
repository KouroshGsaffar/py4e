hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h<=40:
    pay=h*r
else:
    pay=40*r+1.5*r*(h-40)
print(pay)

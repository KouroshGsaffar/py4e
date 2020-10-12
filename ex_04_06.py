def computepay(h,r):
    h=float(h)
    r=float(r)
    if h<=40:
        pay=h*r
        return pay
    else:
        pay=40*r+1.5*r*(h-40)
        return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(hrs,rate)
print("Pay",p)

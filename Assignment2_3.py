# prompt the user for hours and rate

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)

#compute pay

pay = hrs*rate
print("Pay:",pay)

if pay > 100 :
    print("Over Budget")
if pay<= 100 :
    print("Pay Approved")
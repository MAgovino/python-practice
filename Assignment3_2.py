# assignment 3.1

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40 :
    othrs = h % 40
    otrate = r * 1.5
    pay = (40 * r) + (othrs * otrate)
else :
    pay = (h * r)

print(pay)
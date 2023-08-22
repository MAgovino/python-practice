# assignment 4.6 using a defined function

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

def computepay (h,r) :
    if h > 40 :
        othrs = h - 40
        otrate = r * 1.5
        otpay = (40 * r) + (othrs * otrate)
        # print ("OT Pay is: ",otpay)
        return (otpay)
    else :
        regpay = (h * r)
        # print ("RegPay is: ",regpay)
        return (regpay)

pay = computepay (h,r)        
print("Pay",pay)
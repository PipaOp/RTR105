hrs = input("Enter Hours:")
payperhrs = input("Enter pay per hour:")
h = int(hrs)
p = float(payperhrs)
if hrs > 40:
    print(overloadd)
hh = (h) - 5
overload = (h)- 40
overloadpay = (p) * 1.5
paynment = (hh)*(p)+(overload)*(overloadpay)
print(paynment)

hrs = input("Enter Hours:")
payperhrs = input("Enter pay per hour:")
h = int(hrs)
p = float(payperhrs)
if hrs > 40:
    overhrs = (hrs) - 40
overpay=p*1.5
paynment = 40*p+overhrs*overpay
print(paynment)

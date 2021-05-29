def computepay (h, r) :
    print ("In computepay", h, r)
    if h > 40:
        pay = 40 * r + (h - 40)  *  (r * 1.5)
    else:
        pay = hours * rate
    return pay

try :
    hours = float(input ("Enter Hours:"))
except :
    print("Non numeric value detected for hours")
    exit ()
try :
    rate = float(input ("Enter Rate:"))
except :
    print("Non numeric value detected for rate")
    exit()

p = computepay (hours,rate)
print ("Pay", p)

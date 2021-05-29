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
if hours > 40:
    pay = 40 * rate + (hours - 40)  * (rate * 1.5)
else:
    pay = hours * rate
print ("Pay", pay)

number = 0
total = 0
while True :
    value = (input ("Enter number :"))
    if value == "done" :
        break
    try:
        svalue = float (value)
    except:
        print ("Invalid input")
        continue
    number = number + 1
    total = total + svalue

print ("Sum of the numbers:", total)
print ("How many numbers are entered? :", number)
print ("Average :", total / number)

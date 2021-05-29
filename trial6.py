def computegrade (s) :
    if s >= 0.9 :
        return "A"
    elif score >= 0.8 :
        return "B"
    elif score >= 0.7 :
        return "C"
    elif score >=0.6 :
        return "D"
    else :
        return "F"

try :
    score = float ( input ("Enter Score : "))
except :
    print ("Non numeric value detected")
    exit ()

c = computegrade (score)
print ("Grade:", c)

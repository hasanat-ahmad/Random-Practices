weight = float(input("Enter your weight: "))
scale = input("Press K for Kgs or lbs for pounds: ")
if (scale == "K".lower()):
    intoPounds = weight * 2.2
    print("Your weight in pounds is", intoPounds)
elif (scale == "Lbs".lower()):
    
    intoKgs = weight / 2.2
    print("Your weight in Kg is", intoKgs)
else:
    print("Invalid input")
    print(scale)
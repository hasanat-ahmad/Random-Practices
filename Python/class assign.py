while True:
    temp = float(input("Write temperture: \n"))
    if temp < 0:
        print("Freezing")
    elif  0 <= temp <= 15:
        print("Cold")
    elif 15 < temp <= 30:
        print("Warm")
    elif 30 < temp <= 40:
        print("Hot")
    elif temp > 40:
        print("Very hot")

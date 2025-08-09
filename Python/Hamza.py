while True:
    Number = (input("Enter a number: "))
    if (int(Number) % 2 == 0):
        i = 0
        while (i < 51):
            print(i)
            i = i + 2
        
    elif (int(Number) % 2 != 0):
        i = 1
        while (i < 50):
            print(i)
            i = i + 2
    elif (Number == 0):
        break
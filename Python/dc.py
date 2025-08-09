while True:
    import random
    x = random.randint(0,3)
    Number = int(input("Enter a number: "))
    if (Number == x):
        print("You won")
    else:
        print("You failed")
    break
print(x)
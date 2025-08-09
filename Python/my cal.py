while True:
    check = input("Press any key to continue or 0 to exit.\n")
    if check == "0":
        break
    while True:
        operator = input("Press 1 for +, 2 for -, 3 for *, 4 for / \n")
        if operator in ["1","2","3","4"]:
            break
        print("Wrong Operator!")
    first = float(input("Enter first number: \n"))
    second = float(input("Enter second number: \n"))
    if operator == "1":
            print(first + second)
    elif operator == "2":
            print(first - second)
    elif operator == "3":
            print(first * second)
    elif operator == "4":
            if second == 0:
                print("Undefined.")
            else :
                  print(first / second)
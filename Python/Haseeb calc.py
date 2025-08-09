iter_var = 0
while True and iter_var != 3:
    check_var = input("Press any key to contiue and 0 to exit \n")
    if check_var == "0":
        break
    while True:
        operator = input("Press 1 for +, 2 for -, 3 for x, 4 for / \n")
        if operator in ["1","2","3","4"]:
            break
        print("Wrong operator! please check again")
    first = input("Enter the first number: ")
    sec = input ("Enter the second number: ")

    if operator == "1":
        print(float(first)+float(sec))
    elif operator == "2":
        print(float(first)-float(sec))
    elif operator == "3":
        print(float(first)*float(sec))
    elif operator == "4":
      if sec == "0":
          print("Anything divided by zero is undefined. ")
      else:
          print(float(first)/float(sec))
    
    iter_var = iter_var + 1 
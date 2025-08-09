inp = input("Enter password: ")
lower_var = False
upper_var= False
char_var = False
digit_var = False 

for i in inp:
    if i.isupper():
        upper_var = True
    if i.islower():
        lower_var = True
    if i.isdigit():
        digit_var = True
    if not i.isalpha() and not i.isdigit():
        char_var = True

if len(inp) >= 8 and lower_var and upper_var and char_var and digit_var:
    print("Password is strong!")
else:
    print("Paswsword is not strong enough!")
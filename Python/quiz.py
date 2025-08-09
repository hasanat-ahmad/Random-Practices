inp = input("Enter your password: ")
upp = False
low = False
special = False
dig = False
for i in inp:
    if i.isupper():
        upp = True
    if i.islower():
        low = True
    if i.isdigit():
        dig = True
    if not i.isalpha() and not i.isdigit():
        special = True
if len(inp) and upp and low and special and dig:
    print("You have a strong password")
else:
    print("Please enter a strong password")
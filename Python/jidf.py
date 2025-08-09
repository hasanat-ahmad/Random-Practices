sum = 1
n = int(input("Enter a number: "))
for i in range(2,(n//2)+1):
    if (n%i) == 0:
        sum = sum + i
if sum == n:
    print("Perfect number")
else:
    print("Not perfect ")

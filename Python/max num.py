list1 = []
num = int(input("Write total number of elements in the set: "))
for x in range(1,num+1):
    elements = int(input("Write elements: "))
    x = list1.append(elements)
print("The max number is:",max(list1))


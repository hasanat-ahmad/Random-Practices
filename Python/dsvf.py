# # # # # # sum=0
# # # # # # for i in range (2,1001):
# # # # # #     n=True
# # # # # #     for k in range (2,i):
# # # # # #         if i%k==0:
# # # # # #             n=False
# # # # # #             break
# # # # # #     if n==True:
# # # # # #         sum=sum+i
# # # # # # print(sum)

# # # # # # # sum_prime = 0

# # # # # # # for i in range(2, 1001):
# # # # # # #     n = True
# # # # # # #     for k in range(2, i):
# # # # # # #         if i % k == 0:
# # # # # # #             n = False
# # # # # # #             break
# # # # # # #     if n:
# # # # # # #         sum_prime += i

# # # # # # # print(sum_prime)
# # # # # import random
# # # # # def rand_int():
# # # # #     random_int = random.randint(1,20)
# # # # # while True:
# # # # #     inp = int(input("Enter a number between 1 and 20: "))
# # # # #     if inp == random_int:
# # # # #         print("Correct")
# # # # #         break
# # # # #     else:
# # # # #         print("Again")
# # # # # rand_int()

# # # # import random

# # # # def rand_int():
# # # #     return random.randint(1, 20)

# # # # random_int = rand_int()

# # # # while True:
# # # #     inp = int(input("Enter a number between 1 and 20: "))
# # # #     if inp == random_int:
# # # #         print("Correct")
# # # #         break
# # # #     else:
# # # #         print("Try again")

# # # # print("The correct number was:", random_int)

# # # sum = 0
# # # x = int(input("Enter the number to which you want ot add: "))
# # # for i in range(x + 1):
# # #     sum = sum + i
# # # print("Sum:",sum)

# # sum = 0
# # i = 0
# # inp = int(input("Write numbers to be added: "))
# # while i < inp:
# #     i = i + 1
# #     y = (input("Write numbers: "))
# #     z = int(y)
# #     for k in range(z):
# #         sum = sum + k
# # print("Sum:",sum)
# n = int(input('Write a number to be checked: '))
# p = 0
# for i in range(2, n//2):
#     if n%i == 0:
#         p = 1
#         break
# if p:
#     print("Prime")
# else:
#     print("Not Prime")

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

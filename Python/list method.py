import random
def guess_number():
    target_number = random.randint(1, 20)
    while True:
        user_guess = int(input("Enter your guess (between 1 and 20): "))
        if user_guess == target_number:
            print("Well Guessed!")
            break
        else:
            print("Wrong guess. Try again.")
guess_number()



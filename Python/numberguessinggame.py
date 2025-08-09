import random
import math
while True:
    print("WELCOME TO THE NUMBER GUESSING GAME")
    upperlimit=int(input("Enter upper limit for range of numbers: "))
    lowerlimit=int(input("Enter lower limit for range of numbers: "))
    randomnum=random.randint(lowerlimit,upperlimit)
    guesses=round(math.log(upperlimit-lowerlimit+1,2))
    print("You have",guesses,"chances to guess the number.")
    count=0
    while count<guesses:
        guess=int(input("Enter your guess: "))
        if guess==randomnum:
            if count<=guesses:
                print("You have guessed correctly. Congratulations You Win!")
                if count<1:
                    print("It took you",count+1,"guess to guess the number")
                elif count>=1:
                    print("It took you",count+1,"guesses to guess the number")
            break
        elif guess<randomnum:
            count+=1
            if count<guesses:
                print("You have guessed too small. Try again!")
            continue
        elif guess>randomnum:
            count+=1
            if count<guesses:
                print("You have guessed too big. Try again!")
            continue
    if count>=guesses:
        print("You could not guess the number in the required amount of tries. Boohoo You lose!")
        print("The number was",randomnum,",","Tough Luck.")
    startagain=int(input("Do you want to play again? Type 1 for yes or 0 for no: "))
    if startagain==1:
        continue
    if startagain==0:
        break
    quit()
import random

number = random.randint(0,10)
chances = 1
guess = int(input("Try to guess a number : "))
while chances < 6:

    if guess > number:
        print("Try to guess a lower number")

    if guess < number:
        print("Try to guess a higher a number")
    
    if guess == number:
        print("That's correct! You are the champ! The Number was ", number, "and it only took you", chances, "tries!")
        break
    
    if guess != number:
        chances += 1
        print('chances left = ' + str(7-chances))
        guess = int(input("Guess again: "))

    if chances > 4:
        print("You lose! The number is " + str(number))
 









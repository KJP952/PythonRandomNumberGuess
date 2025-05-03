import math
import random

#User Inputs a range
val1 = input("Enter your lower number of range ")
val2 = input("Enter your higher number of range ")
print("Your range " + "(" + val1 + "," + val2 + ")")

val1 = int(val1)
val2 = int(val2)
NumberOfGuesses = 0

#Calculate the maximum number of guesses based on range
MaxGuess = math.log2(val2 - val1 + 1)

#Python selects a random number in range
correctNum = random.randrange(val1, val2)

#User inputs guess
guess = input("Enter your guess ")
guess = int(guess)

#Checks users input and gives back feedback
while(guess != correctNum):

    if(int(NumberOfGuesses) > 0):
        guess = input("Enter your guess ")
        guess = int(guess)

    if(guess > correctNum):
        NumberOfGuesses += 1
        print("Try Again! You guessed too high")

    if(guess < correctNum):
        NumberOfGuesses += 1
        print("Try Again! You guessed too small")

    if(NumberOfGuesses >= MaxGuess):
        print("Better Luck Next Time! The correct number was " + str(correctNum))
        break

    elif(guess == correctNum):
        print("Congratulations! The correct number was " + str(correctNum))

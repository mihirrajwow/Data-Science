import random

randNum = random.randint(1,10)
# print(randNum)
userGuess=None
guesses = 0
while(userGuess!=randNum):
    userGuess = int(input("Enter your Guess: "))
    if userGuess==randNum:
        print(f"Congratulations!! You guessed it RIGHT!!!!!!!!!!!!!!!!!")
        print(f"You took {guesses + 1} guesses.")
    elif userGuess>randNum:
        print(f"(try guessing a lower number)")
    elif userGuess<randNum:
        print(f"(try guessing a higher number)")
    guesses+=1
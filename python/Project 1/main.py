# Snake-Water-Gun or Rock-Paper-Scissors
import random
def gameWin(c,y):
    # If two values are equal, declare a tie!
    if c == y:
        return None
    
    # Check for all possibilities when computer chose s
    elif c == 's':
        if y == 'w':
            return False
        elif y == 'g':
            return True
        
    # Check for all possibilities when computer chose w
    elif c == 'w':
        if y == 'g':
            return False
        elif y == 's':
            return True
        
    # Check for all possibilities when computer chose g
    elif c == 'g':
        if y == 's':
            return False
        elif y == 'w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp,you)

print(f"Computer chose {comp}.")
print(f"You chose {you}.")

# Printing the Game Return
if a == None:
    print("The game is a tie!")
elif a:
    print("You Won!")
else:
    print("You Lose!")
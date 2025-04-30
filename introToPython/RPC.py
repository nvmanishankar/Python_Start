import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)



print("")
playerchoice=input("Enter ...\n 1 for Rock \n 2 for Paper \n 3 for Scissors:\n\n")
player=int(playerchoice)
if player<1 or player>3:
    sys.exit("you must enter 1-3")
computerChoice=random.choice("123")
computer=int(computerChoice)
print("")
print("you choose" + str(RPS(player)).replace('RPS.',''))
print("computer choose" + str(RPS(computer)).replace('RPS.',''))
print("")

if player==1 and computer==3:
    print("You win! Rock crushes Scissors.")
elif player==2 and computer==1:
    print("You win! Paper covers Rock.")
elif player==3 and computer==2:
    print(" Scissors cut Paper.You win!")
elif player==computer:
    print("It's a tie! Both chose the same.")
else:
    print("python wins")

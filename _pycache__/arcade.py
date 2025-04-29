from guess_number import gn
from rps import rps

import sys


def arcade(name='PlayerOne'):
    print("Welcome to the Arcade \n")
    print("1. Guess Number Game")
    print("2. Rock Paper Scissors")
    print("3. Exit to exit arcade")
    welcome_back=False
    while True:
        choice = input("Please enter your choice: ")
        if choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif choice == "2":
            gname = gn(name)
            gname()
        elif choice == "3":
            print("Exiting the arcade. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
        




if __name__=="__main__":
    import argparse
    parse=argparse.ArgumentParser(description="provides which game you wnt t play")
    parse.add_argument(
        "-n","--name",metavar="name",help="enter name"
    )
    args=parse.parse_args()
    arcade=arcade(args.name)
    arcade()

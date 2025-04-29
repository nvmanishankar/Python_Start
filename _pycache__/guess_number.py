import random
import sys
def gn(name='PlayerOne'):
    print(name)
    game_count=0
    player_wins=0
    python_wins=0
    winpercent=0
    def play_gn():
        nonlocal game_count
        nonlocal player_wins
        nonlocal python_wins
        nonlocal winpercent
        nonlocal name
        print("Welcome to the Guess Number Game!\n")
        print("You have to guess a number between 1 and 3.\n")
        print("If you guess correctly, you win!\n")
        print("If you guess incorrectly, Python wins.\n")
        print("Let's start the game!\n")
        systemchoice=random.choice(["1","2","3"])
        userchoice=input(f"{name} guess number which i am thinking of...1,2,or3.")
        def decide_winner(systemchoice,userchoice):
            nonlocal game_count
            nonlocal player_wins
            nonlocal python_wins
            nonlocal winpercent
            nonlocal name
            game_count+=1
            if userchoice not in ["1","2","3"]:
                print(f"{name} please enter a valid nnumber\n")
                return play_gn()
            
            elif userchoice==systemchoice:
                print("You win!")
                player_wins+=1
            
            else:
                print(f"{name}You guessed it wrong!\n")
                print("the correct number was ",systemchoice)
                python_wins+=1

        decide_winner(systemchoice,userchoice)
        print(f"Game Count: {game_count}")
        print(f"Player Wins: {player_wins}")
        print(f"Python Wins: {python_wins}")
        
        if game_count>0:
            winpercent=(player_wins/game_count)*100
            print(f"Win Percentage: {winpercent:.2f}%")
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"{name} Thank you for playing!\n")
            if __name__=="__main__":
                print("Exiting the game. Goodbye!")
                sys.exit("Bye 👋")
            else:
                return
    return play_gn

if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(description="provides a guess a number game")
    parser.add_argument(
        "-n","--name",metavar="name",help="enter name"
        )   
    args=parser.parse_args()
    guess_number=gn(args.name)
    guess_number()


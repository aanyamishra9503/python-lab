import random

ROCK= "r"
PAPER= "p"
SCISSORS="s"

emojis= {ROCK:'🪨', PAPER: '📃', SCISSORS: '✂️'}
choices= tuple(emojis.keys())

def get_user_choice():
     while True:
         user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
         if user_choice in choices:
              return user_choice
         else:
              print("Invalid character")


def show_CHOICES(user_choice, computer_choice):
     print(f"you chose:{emojis[user_choice]}")
     print(f"computer chose: {emojis[computer_choice]}")

def winner(user_choice, computer_choice):
    print(f"DEBUG: user={user_choice}, computer={computer_choice}")  # ← add this
    if user_choice == computer_choice:
        print("tie")
    elif (
        (user_choice == ROCK    and computer_choice == SCISSORS) or
        (user_choice == PAPER   and computer_choice == ROCK)     or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You Win!")
    else:
        print("You Lose!")


def play_game():
     while True:
          user_choice= get_user_choice()
          computer_choice= random.choice(choices)
          show_CHOICES(user_choice, computer_choice)
          winner(user_choice, computer_choice)
          
          continue_ornot= input("Do you want to continue? (y/n): ").lower()
          if continue_ornot== 'n':
               break


play_game()

#REFACTORING--breaking your code into smaller blocks of code....into modules and functions
#computer always wins
#the last block of code of if isnt working
#DRY--Dont Repeat Yourself
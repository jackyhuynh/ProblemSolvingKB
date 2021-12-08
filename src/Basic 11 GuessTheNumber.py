from random import randint

Easy = 10
Hard = 5
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def check_number(guess: int, answer: int):
    if answer > guess:
        print("To low!!!")
        return False
    elif answer < guess:
        print("To high!!!")
        return False
    else:
        print(f"You WIN! The answer is {answer}!!")
        return True
    return


def set_difficulty():
    level = input("Choose a difficulty 'easy' or 'hard': ")
    if level == 'easy':
        return Easy
    else:
        return Hard


def game():
    print(logo)  # Print the logo here
    print("Welcome to the Number Guessing Game!!")  # Welcome String
    print("I am thinking a number between 1 and 100")  # Welcome String
    answer = randint(1, 100)  # Create Random Answer
    turns = set_difficulty()  # Create New Turn
    print(f"You have {turns} attempts remaining to guess the number")  # Create new turn
    guess = 0
    check_cond = False
    while turns > 0 and not check_cond:
        guess = int(input("Enter your guess here: "))
        check_cond = check_number(guess=guess, answer=answer)
        turns -= 1
    if turns == 0:
        print("You are run out of turn!!!")


game()

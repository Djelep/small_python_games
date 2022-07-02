import random


def play():
    choices = ("rock", "paper", "scissors")
    c = random.choice(choices)
    h = input("Please enter rock, paper or scissors ")

    if c == h:
        print("It's a tie")

    if is_win(h, c):
        return "You won!"

    return "You lost!"


def is_win(choice_h, choice_c):
    if (choice_h == "paper" and choice_c == "rock") or (choice_h == "rock" and choice_c == "scissors") \
            or (choice_h == "scissors" and choice_c == "paper"):
        return True


print(play())
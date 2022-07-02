import random


def guess(x):
    secret_number = random.randint(0, x)
    secret = 0
    while secret_number != secret:
        try:
            secret = int(input("Try to guess what number the computer thinks of: "))
        except ValueError:
            print("Please input an integer: ")
            continue
        if secret < secret_number:
            print("Your number is lower than secret")
        elif secret > secret_number:
            print("Your number is bigger than secret")
    print(f"You're right, computer thinks of {secret}")


guess(100)
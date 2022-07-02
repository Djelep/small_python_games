def guess(x):

    # block where user thinks of a number
    secret = 0
    while not secret:
        try:
            secret = int(input(f"Please think of a number between 1 and {x} "))
        except ValueError:
            print("Please enter an integer ")
        if not 1 < secret < x:
            print(f"Please enter a number between 1 and {x} ")
            secret = 0
            continue

    # block where computer is trying to guess the number

    lower = 1
    higher = x
    response = ''
    while response != "yes":
        attempt = (lambda low, high: (high - low) // 2 + low)(lower, higher)
        print(f"The number you think of is {attempt}")
        response = input(": ")
        if response not in ("yes", "lower", "higher"):
            print("Please enter if it is higher, lower or match.")
            continue
        elif response == "lower":
            higher = attempt
        elif response == "higher":
            lower = attempt
    print(f"Congrats, the number is {attempt}")


guess(2000)

import random
import time
import sys

available_choices = ["ROCK", "PAPER", "SCISSORS"]
print("ROCK, PAPER, SCISSORS\n")
# declaring data types for results
wins = 0
losses = 0
ties = 0
while True:
    # printing results and taking input from user
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    user_move = str(input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n")).lower()

    # if quit...
    if user_move == 'q':
        print("Preparing to Exit", end='')
        for i in range(5):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(.5)
        print("\nGame Exited, Thanks for Playing!!!")
        break

    # making r,p,s of user according to list...
    if user_move == 'p':
        user_move = "PAPER"
    elif user_move == 'r':
        user_move = "ROCK"
    elif user_move == 's':
        user_move = "SCISSORS"
    else:
        print("INVALID!! Select from available choices!!\n")
        continue

    # deciding computer's move...
    computer_choice = random.choice(available_choices)

    # printing both choices...
    print(user_move, "versus", end='')
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.3)
    print()
    print(computer_choice)

    # deciding win/lose/tie
    # tie if...
    if user_move == computer_choice:
        ties += 1
        print("It is a tie!")
        continue

    # win if... else lose
    if ((user_move == "ROCK" and computer_choice == "SCISSORS") or (
            user_move == "SCISSORS" and computer_choice == "PAPER") or (
            user_move == "PAPER" and computer_choice == "ROCK")):
        wins += 1
        print("You win!")
        continue
    else:
        losses += 1
        print("You lose!")
        continue

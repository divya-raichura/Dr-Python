import random

print("I am thinking of a number between 1 and 100.")
decision = input("Want to guess it? y for_while yes / n for_while no: ").lower()

while decision == 'y':
    count = 0
    print("\n \tNOTE: You have only 5 chances!\n")
    chances = 5
    random_digit = random.randint(1, 100)
    won = False
    while count < chances:
        guess = int(input(f"Take a guess! (Chances left: {chances - count}): "))
        if guess not in range(1, 101):
            print("Please enter a number in range 1 to 100")
        elif guess in (range(random_digit - 2, random_digit) or range(random_digit + 1, random_digit + 3)):
            print("Just there!")
        elif guess in range(1, random_digit - 2):
            print("Your guess is too low.")
        elif guess in range(random_digit + 3, 101):
            print("Your guess is too high.")
        else:
            count += 1
            won = True
            print(f"Good job! You guessed my number in {count} guesses!")
            break
        count += 1
    # if chances - count == 0:  # what a miracle! was playing it with sis and found a bug which
    #     print("Sorry, You lost the game!")
    # would be impossible to find, that case was so rare
    # bug: when you have last chance, and luckily you guess correct number, then
    # count = 5 and chances - count = 0
    # so tho you won, it also prints you won, but also prints sorry statement!!!
    if not won:
        print(f"Sorry, You lost the game! The number was {random_digit}")
    decision = input("\nWant to play again? y [yes] / n [no]: ").lower()

# can use functions
# can use match

import random

name = input("Enter your name: ")
print(f"Welcome to the game {name}!!")
words = ["apple", "macbook", "opensource", "java", "python", "game", "elon", "jcole", "galaxy"]
word = random.choice(words)
guesses = random.sample(word, 2)
chances = 10
play = input("Press 'y' to start game: ")
# if play == 'y':
#     while chances > 0:
#         won = True
#         for ch in word:
#             if ch in guesses:
#                 print(ch, end=" ")
#             else:
#                 print("_", end=" ")
#                 won = False
#
#         if won:
#             print("\nYou won")
#             print(f"Your score is {chances * 10} out of 100!!!")
#             break
#
#         guess = input("\nGuess a character: ")
#         guesses += guess
#
#         if guess not in word:
#             chances -= 1
#             print("Wrong Answer")
#             print(f"You have {chances} chances left")
#
#         if chances == 0:
#             print("You Lose!")
#             print(f"Word was {word}")
#             break
#     play = input("Do you want to play again? Press 'y' if yes and any other letter if no: ").upper

# Write a dice rolling game program
# Write a python program that keeps asking the user if they want to roll the dice,
# It should ask them to choose a yes/no or y/n as answer
# If the user inputs 'yes' or 'y', generate 2 random dice numbers,
# If the user enters another value rather than 'yes' or 'y' or 'no' or 'n',
# tell them 'Invalid choice!' and continue the game
# If the user inputs 'no' or 'n', tell them 'Thanks for playing!', then terminate the game.

# Solution:
# Ask the user if they want to roll the dice
# If user enters yes, or y generate 2 random dice numbers
# If no,  or n: terminate the game
# If invalid input, tell them 'Invalid choice!' and continue the game
# Use a while loop to keep the game running until the user decides to quit
# Use the random module to generate random numbers
# Use if-elif-else statements to handle user input
import random
while True:
    user_input = input(
        "You wan play abi you no wan play dice? (yes/y or no/n): ").lower()
    if user_input in ['yes', 'y']:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a {dice1} and a {dice2}.")
    elif user_input in ['no', 'n']:
        print("Gerrara here mehn!! Shiit!")
        break
    else:
        print("Invalid choice! Please enter 'yes', 'y', 'no', or 'n'.")

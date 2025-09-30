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
# import random
# while True:
#     user_input = input(
#         "You wan play abi you no wan play dice? (yes/y or no/n): ").lower().strip()
#     if user_input in ['yes', 'y']:
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f"You rolled a {dice1} and a {dice2}.")
#     elif user_input in ['no', 'n']:
#         print("Gerrara here mehn!! Shiit!")
#         break
#     else:
#         print("Invalid choice! Please enter 'yes', 'y', 'no', or 'n'.")

# # ___________REVRSE A STRING____________________
# user_input = input("Enter a string: ")
# reversed_string = user_input[::-1]
# print(f"Reversed string: {reversed_string}")
# # ___________REVRSE A STRING____________________
# ___________REVERSE A GROUP OF WORDS___________
# import qrcode
# user_input = input("Enter a group of words: ")
# words = user_input.split()
# reversed_words = words[::-1]
# reversed_words = ' '.join(reversed(words))
# print(f"Reversed words: {reversed_words}")
# # ___________REVERSE A GROUP OF WORDS___________
# # write a pyhthon program that takes a URL and generate a QR code for the given URL and save QR code in a file
# url = input("Enter a URL: ")
# qr = qrcode.make(url)
# qr.save("qrcode.png")
# print("QR code saved as qrcode.png")


# ___________QR Code program___________
# import qrcode
# data = input("Enter data or URL: ")
# filename = input("Enter preferred filename (with .png or .jpeg extension): ")
# qr = qrcode.QRCode(box_size=10, border=4)
# qr.add_data(data)
# image = qr.make_image(fill_color="black", back_color="white")
# image.save(filename)
# print(f"QR code saved as {filename}")
# ___________QR Code program___________


# Guess game
# Write a program to have the computer randomly select a number between 1 and
# 10, and then prompt the player to guess the number. The program should give
# hints if the guess is too high or too low.

# ______________Guess Game Code____________________
import random
number_to_guess = random.randint(1, 10)
attempts = 0
print("Welcome to the Guessing Game!")
while True:
    user_guess = input(
        "Guess a number between 1 and 10 (or type 'exit' to quit): ")
    if user_guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    try:
        user_guess = int(user_guess)
        attempts += 1
        if user_guess < 1 or user_guess > 10:
            print("Please guess a number within the range of 1 to 10.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10 or 'exit' to quit.")
# ______________Guess Game Code____________________

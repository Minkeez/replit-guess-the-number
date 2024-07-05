#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

def random_number():
  random_number = random.randint(1, 100)
  return random_number

def choose_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  else:
    print("Please type 'easy' or 'hard' only.")
    choose_difficulty()

def guessing(guess_number, correct_number):
  if guess_number == correct_number:
    return 1
  elif guess_number > correct_number:
    print("Too High.")
    return 0
  else:
    print("Too Low.")
    return 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
correct_number = random_number()
print(f"Pssst, the correct answer is {correct_number}")
attempts = choose_difficulty()

while attempts != 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess_number = int(input("Make a guess: "))
  guess = guessing(guess_number, correct_number)
  if guess == 0:
    attempts -= 1
    if attempts != 0:
      print("Guess again.")
    else:
      print("You've run out of guesses, you lose.")
      break
  else:
    print(f"You got it! The answer was {correct_number}")
    break
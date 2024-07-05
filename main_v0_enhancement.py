from art import logo
import random

def generate_random_number():
  return random.randint(1, 100)

def choose_difficulty():
  while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
      return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid input. Please type 'easy' or 'hard' only.")

def check_guess(guess_number, correct_number):
  if guess_number == correct_number:
    return "correct"
  elif guess_number > correct_number:
    return "Too High."
  else:
    return "Too Low."

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
correct_number = generate_random_number()
print(f"Pssst, the correct answer is {correct_number}")
attempts = choose_difficulty()

while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  try:
    guess_number = int(input("Make a guess: "))
  except ValueError:
    print("Please enter a valid number.")
    continue

  result = check_guess(guess_number, correct_number)

  if result == "correct":
    print(f"You got it! The answer was {correct_number}")
    break

  else:
    print(result)
    attempts -= 1
    
    if attempts == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("Guess again.")
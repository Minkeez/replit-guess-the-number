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

def provide_hint(corrent_number, attempts_left, total_attempts):
  # Provide hints every 3 incorrect guesses
  if (total_attempts - attempts_left) % 3 == 0 and attempts_left != total_attempts:
    # Randomly select a hint type to provide
    hint_type = random.choice(["range", "even_odd", "divisibility"])

    if hint_type == "range":
      range_hint = 10 # Hint range size
      lower_bound = max(1, correct_number - range_hint)
      upper_bound = min(100, correct_number + range_hint)
      print(f"Hint: The number is between {lower_bound} and {upper_bound}.")

    elif hint_type == "even_odd":
      if correct_number%2 == 0:
        print("Hint: The number is even.")
      else:
        print("Hint: The number is odd.")

    elif hint_type == "divisibility":
      divisible_by = random.choice([3, 5])
      if correct_number % divisible_by == 0:
        print(f"Hint: The number is divisible by {divisible_by}.")
      else:
        print(f"Hint: The number is not divisible by {divisible_by}.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
correct_number = generate_random_number()
# just for test
# print(f"Pssst, the correct answer is {correct_number}")
attempts = choose_difficulty()
total_attempts = attempts

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

    provide_hint(correct_number, attempts, total_attempts)

    if attempts == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("Guess again.")
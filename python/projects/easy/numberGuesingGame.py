import random

min = 1
max = 100
answer = random.randint(min, max)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {min} and {max}")

while is_running:
  guess = input("Enter your guess ")
  # возвращает True, если все символы в строке являются цифрами.
  if guess.isdigit():
    guess = int(guess)
    guesses += 1

    if guess < min or guess > max:
      print("That number is out of range")
      print(f"Please select a number between {min} and {max}")
    elif guess < answer:
      print("Too low! Try again!")
    elif guess > answer:
      print("Too high! Try again!")
    else:
      print(f'CORRECT! The answer was {answer}')
      print(f'Number of guesses: {guesses}')
      is_running = False
      
  else:
    print("Invalid guess")
    print(f"Please select a number between {min} and {max}")
import random

word=("apple", "banana", "coconut", "orange", "mango")

hangman_art = {
  0: ("  +---+",
      "  |   |",
      "      |",
      "      |",
      "      |",
      "      |"
     ),
  1: ("  +---+",
      "  |   |",
      "  O   |",
      "      |",
      "      |",
      "      |"
     ),
  2: ("  +---+",
      "  |   |",
      "  O   |",
      "  |   |",
      "      |",
      "      |"
      ),
  3: ("  +---+",
      "  |   |",
      "  O   |",
      " /|   |",
      "      |",
      "      |"
     ),
  4: ("  +---+",
      "  |   |",
      "  O   |",
      " /|\\ |",
      "      |",
      "      |"
     ),
  5: ("  +---+",
      "  |   |",
      "  O   |",
      " /|\\ |",
      " /    |",
      "      |"
     ),
  6: ("  +---+",
      "  |   |",
      "  O   |",
      " /|\\ |",
      " / \\ |",
      "      |"
    )
}

def display_guess(wrong_guess):
  print("*"*15)
  for line in hangman_art[wrong_guess]:
    print(line)
    print("********")
  
def display_hint(hint):
  print(" ".join(hint))
    
def display_answer(answer):
  print(" ".join(answer))

def main():
  answer = random.choice(word)
  hint = ["-"] * len(answer)
  wrong_guess = 0
  guessed_letter = set()
   
  is_running = True
  while is_running:
    display_guess(wrong_guess)
    display_hint(hint)
    guess = input("the the letter:").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("invalid syntax")
      continue

    if guess in guessed_letter:
      print(f"{guess}is already used")
      guessed_letter.add(guess)

    if guess in answer:
      for i in range (len(answer)):
        if answer[i] == guess:
          hint[i] = guess
    else:
      wrong_guess += 1

if __name__ == "__main__":  
    main()
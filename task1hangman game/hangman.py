import random

# List of words
words = ["python", "apple", "computer", "camera", "student"]

# Select a random word
word = random.choice(words)

# Empty list for guessed letters
guessed_letters = []

# Number of wrong guesses allowed
attempts = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)
print("Guess the word one letter at a time.")
print("You have", attempts, "wrong guesses.\n")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Remaining Attempts:", attempts)

# Game Over
if attempts == 0:
    print("The correct word was:", word)
    print("\nGame Over!")
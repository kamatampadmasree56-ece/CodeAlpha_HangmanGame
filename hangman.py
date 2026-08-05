import random

# List of predefined words
words = ["python", "apple", "computer", "coding", "laptop"]

# Hangman stages
hangman_stages = [
'''
 +---+
 |   |
     |
     |
     |
     |
========
''',
'''
 +---+
 |   |
 O   |
     |
     |
     |
========
''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
========
''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
========
''',
'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========
''',
'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========
''',
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
'''
]

def play_game():
    secret_word = random.choice(words)
    display = ["_"] * len(secret_word)
    guessed_letters = []
    attempts = 6

    print("=" * 45)
    print("         HANGMAN GAME")
    print("      CodeAlpha Internship")
    print("     Developed by Padmasree")
    print("=" * 45)

    while attempts > 0 and "_" in display:

        print(hangman_stages[6 - attempts])
        print("Word:", " ".join(display))
        print("Attempts Left:", attempts)
        print("Guessed Letters:", " ".join(guessed_letters))

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1:
            print("❌ Please enter only ONE letter.\n")
            continue

        if not guess.isalpha():
            print("❌ Please enter only alphabets.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
            print("✅ Correct!\n")
        else:
            attempts -= 1
            print("❌ Wrong Guess!\n")

    if "_" not in display:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
    else:
        print(hangman_stages[6])
        print("\n💀 Game Over!")
        print("The correct word was:", secret_word)


while True:
    play_game()

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for playing Hangman!")
        break
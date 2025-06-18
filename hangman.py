import random

# Word list with hints
words_with_hints = [
    ("python", "A popular programming language."),
    ("elephant", "A large mammal with a trunk."),
    ("guitar", "A musical instrument with strings."),
    ("astronaut", "A person who travels in space."),
    ("pizza", "Popular Italian dish with cheese.")
]

# Choose a word randomly
word, hint = random.choice(words_with_hints)
guessed = ["_"] * len(word)
attempts_left = 6
guessed_letters = []

print("🕹️ Welcome to Hangman!")
print("Hint:", hint)

while attempts_left > 0 and "_" in guessed:
    print("\nWord: ", " ".join(guessed))
    print("Guessed Letters:", " ".join(guessed_letters))
    print(f"Attempts Left: {attempts_left}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i, char in enumerate(word):
            if char == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1

# End result
print("\n--- GAME OVER ---")
if "_" not in guessed:
    print("🎉 You won! The word was:", word)
else:
    print("💀 You lost! The word was:", word)

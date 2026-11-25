import random

print("Welcome to Hangman Game!")
print("Guess the hidden word.")
print("You have 6 chances.")

words = ["python", "computer", "laptop", "coding", "program"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
chances = 6

while chances > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Chances left:", chances)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong guess!")
        chances -= 1

if "_" not in guessed_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)

else:
    print("\nGame Over!")
    print("The word was:", word)

print("Thanks for playing!")
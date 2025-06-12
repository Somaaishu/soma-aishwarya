import random

def hangman():
    # Predefined list of 5 words
    words = ["apple", "banana", "orange", "grape", "melon"]
    
    # Select a random word
    secret_word = random.choice(words)
    guessed_letters = []
    tries = 6  # Maximum incorrect guesses
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters. You have {tries} tries.")
    print("Guess the word one letter at a time.\n")
    
    while tries > 0:
        # Display current progress with blanks for unguessed letters
        display = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print(" ".join(display))
        
        # Check if player won
        if '_' not in display:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return
        
        # Get and validate player's guess
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("Correct!")
        else:
            tries -= 1
            print(f"Wrong! You have {tries} tries left.")
    
    # If we get here, player ran out of tries
    print(f"\nGame over! The word was: {secret_word}")

# Start the game
if __name__ == "__main__":
    hangman()
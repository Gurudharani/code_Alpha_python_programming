import random

def choose_word():
    words = ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon", "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6
    
    print("Guess the word! Hint: It's a fruit!")
    
    while tries > 0:
        print(display_hangman(tries))
        display_word = " ".join([char if char in guessed_letters else "_" for char in word])
        print(display_word)
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        if guess not in word:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")
        
        if all(char in guessed_letters for char in word):
            print(f"Congratulations! You guessed the word: {word}")
            return
    
    print(display_hangman(tries))
    print(f"You lost! The word was '{word}'.")

if __name__ == "_main_":
    play_hangman()
import random
def choose_word():
    words = ['aviation','debug','Discord','keyboard','cessna', 'piper','cherokee','coding','game','runway','Pharaoh','Exotic','Submerge','Python','Xylophone','Rubik','Mystique','Gazebo','Kaleidoscope','Flabbergasted']
    return random.choice(words) 

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word
def draw_hangman(stage):
    stages = [
        """
         _________
         |      |
         |
         |
         |
        _|_
        """,
        """
         _________
         |      |
         |      O
         |
         |
        _|_
        """,
        """
         _________
         |      |
         |      O
         |      |
         |
        _|_
        """,
        """
         _________
         |      |
         |      O
         |     /|
         |
        _|_
        """,
        """
         _________
         |      |
         |      O
         |     /|\\
         |
        _|_
        """,
        """
         _________
         |      |
         |      O
         |     /|\\
         |     /
        _|_
        """,
        """
         _________
         |      |
         |      O
         |     /|\\
         |     / \\
        _|_
        """
    ]
    print(stages[stage])

def hangman():
    max_attempts = 6
    word = choose_word()
    guessed_letters = []
    attempts = 0 

    print("Hey! Welcome to Hangman: Random Words Edition!")
    print(display_word(word, guessed_letters))

    while attempts < max_attempts:
        guess = input("Guess a letter yo!:").lower()

        if guess in guessed_letters:
            print("That letter was already guessed! Try again.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            guessed_letters.append(guess)
            if guess in word:
                print("Good guess!")
                if display_word(word, guessed_letters) == word:
                    print ("Congratulations! You guessed the word! The word was:", word)
                    return
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                if remaining_attempts ==1:
                    print("Incorrect. You have 1 attempt left")
                else:
                    print("That word was wrong. You have", remaining_attempts, "attempts left.")
                draw_hangman(attempts)
        print(display_word(word, guessed_letters))
    if attempts ==max_attempts:
        print("Sorry, you ran out of attempts. The word was:", word)

def main():
    while True:
        hangman()
        play_again = input("Hey, do you want to play again? (yes/no):").lower()
        if play_again != 'yes':
            break
    print("No problem. Thanks for playing!")
    

if __name__ == "__main__":
    main()


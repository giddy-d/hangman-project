# flask application script

from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

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
    return stages[stage]

@app.route('/')
def index():
    word = choose_word()
    guessed_letters = ""
    attempts = 0 
    max_attempts = 6
    hangman_state = draw_hangman(0)

    return render_template("indexHman.html", word=word, guessed_letters=guessed_letters, attempts=attempts, max_attempts=max_attempts, hangman_state=hangman_state, gameover=False)

@app.route('/play', methods=['POST'])
def play():
    word = request.form["word"]
    guessed_letters = request.form['guessed_letters']
    attempts = int(request.form['attempts'])
    max_attempts = int(request.form['max_attempts'])
    guess = request.form['guess']

    if guess in guessed_letters:
        message = "That letter was already guessed! Try again."
    elif len(guess) != 1 or not guess.isalpha():
        message = "Please enter a single letter."
    else:
        guessed_letters += guess
        if guess in word:
            if display_word(word, guessed_letters) == word:
                message = f"Congratulations! You guessed the word: {word}"
            else:
                message = display_word(word, guessed_letters)
        else:
            attempts += 1
            if attempts == max_attempts:
                message = f"Sorry, you ran out of attempts. The word was: {word}"
            else:
                message = f"Incorrect. You have {max_attempts - attempts} attempts left."

    hangman_state = draw_hangman(attempts)
    
    return render_template('indexHman.html', message=message, word=word, guessed_letters=guessed_letters, attempts=attempts, max_attempts=max_attempts, hangman_state=hangman_state)

if __name__ == '__main__':
    app.run(debug=True)

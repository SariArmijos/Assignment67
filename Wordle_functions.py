#Import random library to access randm.choice function
import random

#Functions

#choose_word() – Selects and returns a secret word.
def choose_word(random_list) :
    #save the computer's choice in a variable
    random_word = random.choice(random_list)
    #return the variable
    return random_word

#get_guess() – Gets and validates the player’s guess, including that previous guesses are rejected
def get_guess() :
    #In case user inserts guess in other than lowercase
    guess = input('Please guess a 5 letter word: ').lower()
    #Take user to a loop until they choose a 5 letter word
    while len(guess) != 5 :
        guess = input('Invalid word. Please guess a 5 letter word: ').lower()
    return guess

#evaluate_guess() – Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess, random_word) :
    feedback = ''
    #Access each letter of the computer's and user's choice
    for i in range(5) :
    #Compare each letter to the right position
        if guess[i] == random_word[i] :
            feedback += ' G '
        elif guess[i] in random_word :
            feedback += ' Y '
        elif guess[i] not in random_word :
            feedback += ' - '
    return feedback

#display_guess() – Displays the guess and its feedback
def display_guess(guess, feedback) :
    print('Guess: ' + guess)
    print('Feedback: ' + feedback)

#has_won() – Determines whether the player has guessed the word
def has_won(guess, random_word) :
    if guess == random_word :
        return True
    else :
        return False
   
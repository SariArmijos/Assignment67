#Import all functions since we will use them all
from Wordle_functions import *

#Create a list with random words to use
random_list = ['align', 'smart', 'logic', 'focus', 'value', 'quest', 'drive', 'beach', 'heart' ]

#1. Welcome the player.
print('\nWelcome to the Mystery Wordle!')
print('Guess the five-letter word\n')
print('G = correct letter and position')
print('Y = correct letter, wrong position')
print('- = letter is not in the word\n')
#Ask if they want to play
answer = input('Would you like to play? (yes/no): ').lower()
while answer == 'yes' :
    #2. Select a secret five-letter word.
    random_word = choose_word(random_list)
    #3. Give the player up to six guesses.
    print('\nYou have up to 6 guesses, use them wisely ;)')
    #Create list to store each guess
    previous_guesses = []
    for round in range(6) :
        #Keep track of the number of rounds. Add 1 to avoid getting round = 0
        round = round + 1
        #Print in which round they are
        print(f'\nAttempt {round} of 6')
        #4. Require each guess to contain exactly five letters.
        guess = get_guess()
        #5. Reject guesses that have already been used.
        while guess in previous_guesses :
            print('You have previously guessed that word, try again')
            #Make sure to use the function that validates the word has 5 letters
            guess = get_guess()
        #Add the guess to the list to compare with future guesses
        previous_guesses.append(guess)
        #6. Display feedback after every guess.
        #Put a gap 
        print()
        feedback = evaluate_guess(guess, random_word)
        #7. Tell the player when a letter is correct, misplaced, or absent.
        display_guess(guess, feedback)
        #8. End the game when the player guesses the word or uses all six attempts.
        if has_won(guess, random_word) :
            print('You won! :D')
            #Stop the for loop once the player has guessed the word
            break
    #Use else statement if the user ends the loop (guesses 6 times) and does guess the right word
    else :
        #9. Display the secret word if the player loses.
        print('You ran out of guesses :( the secret word was "' + random_word + '"')
    #10. Ask whether the player would like to play again
    answer = input('Would you like to play again? (yes/no): ').lower()
#If the player does not want to play take them out of the loop to end game
print('Thanks for playing')
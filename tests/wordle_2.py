# Wordle Game
# Game to guess a five letter within five guesses based upon the user's input


import random
import sys
import time
from tqdm import tqdm


def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words


def select_word(filename): # Select the secret word to guess from Wordle's official dictionary/word selection
    with open(filename) as f:
        words = [line.strip() for line in f]
    word = random.choice(words)
    return word
        

# Checks the assortment and validity of the user's guess/input
def check_if_valid(guess, guesses):
    for i in tqdm(range(74)): # Loading bar for one second
        time.sleep(1/74)
    print('Nice guess!')
    
    return len(guess) == 5 and guess in guesses


# Iterates through the secret word and checks if each letter matches the letters and if they are positioned correcly
def check_arrangement(guess, word): 
    letter = 0
    if letter < len(word):
        for char in range(len(guess)):
            if guess[char] == word[letter]:
                print('✅', end=' ')
            elif guess[char] in word:
                print('🟨', end=' ')
            else:
                print('❌', end=' ')
            letter += 1
    print('\n-- -- -- -- --')


# Checks if the guess is the secret word
def check_guess(guess, word):
    if guess == word: 
        return True
    return False
    
    
def main():
    print('Welcome to Wordle!\nThe objective is to guess a five letter word within five guesses!\nBest of luck!\nIf you would like to quit at anytime please type "Q"')
    print('''              __      __                .___.__          
             /  \    /  \___________  __| _/|  |   ____  
             \   \/\/   /  _ \_  __ \/ __ | |  | _/ __ \ 
              \        (  <_> )  | \/ /_/ | |  |_\  ___/ 
               \__/\  / \____/|__|  \____ | |____/\___  >
                    \/                   \/           \/ ''')
    
    guesses = load_dictionary("guesses.txt")
    word = select_word("answers.txt")
    num_guesses = 0
    while True:
        try:
            guess = input('Guess: ').lower()
            num_guesses += 1
            
            if guess == 'q':
                sys.exit('Exiting the game')
            
            if check_if_valid(guess, guesses):
                check_arrangement(guess, word)
                if check_guess(guess, word):
                    print(f'You guessed the correct word in {num_guesses} guesses! Congratulations!')
                    break
                else:
                    print('That is not the correct word. Please try again')
                    pass
                
            if num_guesses == 5:
                sys.exit(f'The correct word to guess was: {word}')
            
        except ValueError:
            print('This is not a word!') # Error handles numbers
            
        except IndexError:
            print('The word does not consist of five letters!') # Error handles words that are not five letters in length
    
    
if __name__ == '__main__':
    main()
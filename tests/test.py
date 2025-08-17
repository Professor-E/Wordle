# Test for the wordle rearrangement function

import random

words = ['hello', 'tests', 'funny', 'pytho']
word = random.choice(words)
print(word)


def rearrangement(guess, word):
    letter = 0
    for char in range(len(guess)):
        if guess[char] == word[letter]:
            print('Match')
        elif guess[char] in word:
            print('Letter in word')
        else:
            print('No match')
        letter += 1
        
        if letter == len(word):
            break
  
  
def main():
    guess = input('Guess: ')
    rearrangement(guess, word)
    
    
if __name__ == '__main__':
    main()
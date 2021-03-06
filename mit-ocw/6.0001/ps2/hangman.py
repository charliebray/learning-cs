# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import os
import sys

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(os.path.join(sys.path[0], "words.txt"), "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
      if char not in letters_guessed:
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_str = ""
    for char in secret_word:
      if char in letters_guessed:
        guessed_str += char
      else:
        guessed_str += "_ "
    return guessed_str

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    not_guessed_str = ""
    for char in string.ascii_lowercase:
      if char not in letters_guessed:
        not_guessed_str += char
    return not_guessed_str

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')

    num_guesses = 6
    warning_count = 3
    letters_guessed = []

    while num_guesses > 0:

      print('-------------')
      print(f'You have {num_guesses} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')

      guess_letter = input('Please guess a letter: ')

      # Check if guess satisfies does not satisfy guessing requirements.
      if str.isalpha(str.lower(guess_letter)) == False or len(guess_letter) != 1:
        if warning_count > 0:
          warning_count -= 1
          print(f'Oops! That is not a valid letter. You have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          num_guesses -= 1
          print(f'Oops! That is not a valid letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}')
        continue

      # Check if guess has already been guessed before.
      if guess_letter in letters_guessed:
        if warning_count > 0:
          warning_count -= 1
          print(f'Oops! You have already guess that letter. You have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          num_guesses -= 1
          print(f'Oops! You have already guess that letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}')
        continue

      # If guess satisfies criteria, then append to letters guessed.
      letters_guessed.append(guess_letter)
      if guess_letter in secret_word:
        print(f'Correct! That letter is in my word: {get_guessed_word(secret_word, letters_guessed)}')
      else:
        print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
        if guess_letter in ['a', 'i', 'u', 'e', 'o']:
          num_guesses -= 2
        else:
          num_guesses -= 1

      # If the whole word is guessed, finish the game!
      if is_word_guessed(secret_word, letters_guessed) == True:
        print(f'Congratulations, you won!')
        print(f'Your total score for this game is: {(num_guesses) * len(set(secret_word))}')
        return

    print(f'Sorry, you ran out of guesses. The word was {secret_word}.')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = ''.join(my_word.split(' '))
    if len(my_word) != len(other_word):
      return False
    for index in range(0, len(my_word)):
      char = my_word[index]
      if char == '_':
        continue
      if char != other_word[index]:
        return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    temp_list = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        temp_list.append(word)

    if len(temp_list) == 0:
      print('No matches found')
    else:
      print(' '.join(temp_list))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')

    num_guesses = 6
    warning_count = 3
    letters_guessed = []

    while num_guesses > 0:

      print('-------------')
      print(f'You have {num_guesses} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')

      guess_letter = input('Please guess a letter: ')

      # Provide a guess if desired
      if guess_letter == '*':
          show_possible_matches(get_guessed_word(secret_word, letters_guessed))
          continue

      # Check if guess satisfies does not satisfy guessing requirements.
      if str.isalpha(str.lower(guess_letter)) == False or len(guess_letter) != 1:
        if warning_count > 0:
          warning_count -= 1
          print(f'Oops! That is not a valid letter. You have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          num_guesses -= 1
          print(f'Oops! That is not a valid letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}')
        continue

      # Check if guess has already been guessed before.
      if guess_letter in letters_guessed:
        if warning_count > 0:
          warning_count -= 1
          print(f'Oops! You have already guess that letter. You have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          num_guesses -= 1
          print(f'Oops! You have already guess that letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}')
        continue

      # If guess satisfies criteria, then append to letters guessed.
      letters_guessed.append(guess_letter)
      if guess_letter in secret_word:
        print(f'Correct! That letter is in my word: {get_guessed_word(secret_word, letters_guessed)}')
      else:
        print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
        if guess_letter in ['a', 'i', 'u', 'e', 'o']:
          num_guesses -= 2
        else:
          num_guesses -= 1

      # If the whole word is guessed, finish the game!
      if is_word_guessed(secret_word, letters_guessed) == True:
        print(f'Congratulations, you won!')
        print(f'Your total score for this game is: {(num_guesses) * len(set(secret_word))}')
        return

    print(f'Sorry, you ran out of guesses. The word was {secret_word}.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = 'addle' #choose_word(wordlist)
    hangman_with_hints(secret_word)

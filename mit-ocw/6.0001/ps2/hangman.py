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

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
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
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_ "
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_not_guessed = ""
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            letters_not_guessed += char
    return letters_not_guessed

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

    # Loop until the user has guessed the word or run out of guesses
    num_guesses = 6
    warning_count = 3
    letters_guessed = list()
    print(f'You have {warning_count} warnings left.')
    print('-------------')
    while num_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        # Tell the user how many guesses are left and the available letters
        print(f'You have {num_guesses} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')

        # User inputs a guess
        letter_guess = input('Please guess a letter: ').lower()

        # Check if the letter_guess is indeed a letter
        if letter_guess not in string.ascii_lowercase:
            if warning_count < 1:
                print(f'Oops! That is not a valid letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}')
                num_guesses -= 1
                continue
            warning_count -= 1
            print(f'Oops! That is not a valid letter. You have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        # Check if the letter has been guessed before
        elif letter_guess in letters_guessed:
            if warning_count < 1:
                print(f"Oops! You've already guess that letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}")
                num_guesses -= 1
                continue
            warning_count -= 1
            print(f"Oops! You've already guess that letter. You now have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            letters_guessed.append(letter_guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guess in secret_word:
                print(f'Good guess: {guessed_word}')
            else:
                print(f'Oops! That letter is not in my word: {guessed_word}')
                if letter_guess in ['a', 'e', 'i', 'o', 'u']:
                  num_guesses -= 2
                else:
                  num_guesses -= 1
        print('-------------')

    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print(f'Your total score for this game is: {num_guesses * len(set(secret_word))}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

    return None

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
    my_word = my_word.replace(' ', '')
    char_list = list()
    if len(my_word) != len(other_word):
        return False
    for i in range(0, len(my_word)):
        # If unknown letter, then add it to char_list
        if my_word[i] == '_':
            char_list.append(other_word[i])
        elif my_word[i] != other_word[i] or other_word[i] in char_list:
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
    match_counter = 0
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            print(f'{other_word} ')
            match_counter += 1
    if match_counter == 0:
        print('No matches found')
    return None


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

    # Loop until the user has guessed the word or run out of guesses
    num_guesses = 6
    warning_count = 3
    letters_guessed = list()
    print(f'You have {warning_count} warnings left.')
    print('-------------')
    while num_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        # Tell the user how many guesses are left and the available letters
        print(f'You have {num_guesses} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')

        # User inputs a guess
        letter_guess = input('Please guess a letter: ').lower()

        # Check if the input is an asterick
        if letter_guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print('-------------')
            continue

        # Check if the letter_guess is indeed a letter
        if letter_guess not in string.ascii_lowercase:
            if warning_count < 1:
                print(f'Oops! That is not a valid letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}')
                num_guesses -= 1
                continue
            warning_count -= 1
            print(f'Oops! That is not a valid letter. You have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        # Check if the letter has been guessed before
        elif letter_guess in letters_guessed:
            if warning_count < 1:
                print(f"Oops! You've already guess that letter. You have 0 warnings left, and lose a guess: {get_guessed_word(secret_word, letters_guessed)}")
                num_guesses -= 1
                continue
            warning_count -= 1
            print(f"Oops! You've already guess that letter. You now have {warning_count} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            letters_guessed.append(letter_guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guess in secret_word:
                print(f'Good guess: {guessed_word}')
            else:
                print(f'Oops! That letter is not in my word: {guessed_word}')
                if letter_guess in ['a', 'e', 'i', 'o', 'u']:
                  num_guesses -= 2
                else:
                  num_guesses -= 1
        print('-------------')

    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print(f'Your total score for this game is: {num_guesses * len(set(secret_word))}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

    return None



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #secret_word = 'tact'
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

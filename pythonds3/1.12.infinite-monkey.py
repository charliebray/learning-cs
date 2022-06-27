from random import randrange

desired_str = 'methinks it is like a weasel'

def random_letter():

    '''
    Returns a random letter froma list of characters.
    '''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    random_index = randrange(0, len(alphabet))
    return alphabet[random_index]

def random_sentence():

    '''
    Returns a random sentence 28 characters long (monkey bashing).
    '''

    random_sentence = ''
    for _ in range(0,28):
        random_str = random_letter()
        random_sentence += random_str
    return random_sentence

def score():

    '''
    Generate random sentence and give a score.
    '''

    score = 0
    counter = 0
    best_score = -1

    while score < 100:
        score = 0
        random_str = random_sentence()
        for index in range(len(random_str)):
            if random_str[index] == desired_str[index]:
                score += 1.
        score = 100*float(score)/len(random_str)

        if score > best_score:
            best_guess = random_str
            best_score = score

        counter += 1
        if counter % 1000 == 0:
            print(f'Number of tries: {counter}, Best word: {best_guess}, Best score: {best_score}')

def main():
    
    '''
    A hill climbing algorithm for the infinite monkey problem.
    '''

    initial_guess = random_sentence()
    final_guess = []

    for index in range(0, len(initial_guess)):
        correct_letter, guess_letter = desired_str[index], initial_guess[index]
        while correct_letter != guess_letter:
            guess_letter = random_letter()
        final_guess.append(guess_letter)
        print(''.join(final_guess))

main()
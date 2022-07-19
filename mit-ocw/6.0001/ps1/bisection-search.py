def main():
    cube = -0.2
    epsilon = 0.001
    num_guesses = 0

    if abs(cube) < 1:
        low = abs(cube)
        high = 1
    else:
        low = 0
        high = abs(cube)

    guess = (high + low)/2.0

    while abs(guess**3 - abs(cube)) >= epsilon:
        if guess**3 < abs(cube):
            low = guess
        else:
            high = guess

        print(guess)

        guess = (high + low)/2.0
        num_guesses += 1

    # solve for negative cases
    if cube < 0:
        guess = -guess

    print(f'num_guesses = {num_guesses}')
    print(f'{guess} is close to the cube root of {cube}')

if __name__ == '__main__':
    main()
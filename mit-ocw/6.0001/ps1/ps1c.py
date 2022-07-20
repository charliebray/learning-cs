def savings_func(annual_salary, portion_saved):
    semi_annual_raise = 0.07
    current_savings = 0

    for num_months in range(1, 37):
        current_savings = current_savings * (1 + 0.04/12)
        current_savings += annual_salary * portion_saved / 12
        if num_months % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)

    return current_savings

def main():
    annual_salary = float(input('Enter your annual salary: '))
    lower_bound = 0
    upper_bound = 10000
    guess = (lower_bound + upper_bound)/2.0
    required_amount = 2.5 * 10**5

    if savings_func(annual_salary, 1.0) < required_amount:
        return print(f'It is not possible to pay the down payment in three years.')

    num_guesses = 0
    while abs(savings_func(annual_salary, round(guess/10000., 4)) - required_amount) >= 100:
        if savings_func(annual_salary, guess/10000.) < required_amount:
            lower_bound = guess
        else:
            upper_bound = guess
        guess = (lower_bound + upper_bound)/2.0
        num_guesses += 1

    print(f'Best Savings Rate: {round(guess/10000., 4)}')
    print(f'Steps in bisection search: {num_guesses}')

if __name__ == '__main__':
    main()
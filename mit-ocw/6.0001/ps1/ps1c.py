def calculate_savings(
        current_savings: float,
        annual_rate: float,
        annual_salary: float,
        portion_saved: float,
        semi_annual_raise: float,
        num_months: int
    ) -> float:
    """
    Calculate the savings after a certain number of months.

    Args:
        current_savings (float): The total amount of money currently saved
        annual_rate (float): The annual rate of return on savings represented as a decimal.
        annual_salary (float): The annual salary represented as a float.
        portion_saved (float): The proportion of annual salary that is saved.
        semi_annual_raise (float): The proportional raise of annual salary every 6 months.
        num_months (int): The number of months we have saved for.

    Returns:
        float: The amount saved after num_months.
    """
    for i in range(1, num_months+1):
        # How much is saved each month
        monthly_saved = annual_salary * portion_saved
        current_savings += monthly_saved/12 + current_savings*(annual_rate/12)
        # Every 6 months, give yourself a raise
        if i % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
    return current_savings


def bisection_search(annual_salary: float) -> None:
    """
    A bisectional search to find the proportion required to save for the down payment in 36 months, given a salary.

    Args:
        annual_salary (float): The annual salary represented as a float.

    Returns:
        None
    """
    # Parameters given for this problem
    semi_annual_raise = 0.07
    annual_rate = 0.04
    down_payment = 0.25 * 10**6
    current_savings = 0
    num_months = 36

    # Edge case
    portion_saved_max = 1
    max_savings = calculate_savings(
        current_savings, annual_rate, annual_salary,
        portion_saved_max, semi_annual_raise, num_months
    )
    if max_savings < down_payment:
        print('It is not possible to pay the down payment in three years.')
        return None

    # Bisectional search
    min = 0
    max = 1
    savings = 0
    num_steps = 0
    while abs(savings - down_payment) > 100:
        # Our guess
        portion_saved_guess = (min + max)/2.
        # Determine how much we've saved given our guess
        savings = calculate_savings(
            current_savings, annual_rate, annual_salary,
            portion_saved_guess, semi_annual_raise, num_months
        )
        # If our savings are too high, we need to guess a lower portion
        if savings > down_payment:
            max = portion_saved_guess
        # If our savings are too low, we need to guess a higher portion
        else:
            min = portion_saved_guess
        # Count the number of iterations
        num_steps += 1
    print(f'{round(portion_saved_guess, 4)}')
    print(f'{num_steps}')
    return None


if __name__ == '__main__':
    annual_salary = float(input('Enter your starting salary: '))
    bisection_search(annual_salary)

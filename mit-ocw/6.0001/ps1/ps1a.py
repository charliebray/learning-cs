def months_to_save(
        total_cost: float,
        portion_down_payment: float,
        current_savings: float,
        annual_rate: float,
        annual_salary: float,
        portion_saved: float
    ) -> int:
    """
    Calculate the number of months required to save for a down payment on a home.

    Args:
        total_cost (float): The total cost of the home.
        portion_down_payment (float): The percentage of total cost for a down payment represented as a decimal.
        current_savings (float): The total amount of money currently saved
        annual_rate (float): The annual rate of return on savings represented as a decimal.
        portion_saved (float): The proportion of annual salary that is saved.

    Returns:
        int: The number of months required to save for a down payment.
    """
    num_months = 0
    # Down payment required for the home
    down_payment = total_cost * portion_down_payment
    # How much is saved each month
    monthly_saved = annual_salary * portion_saved
    while current_savings < down_payment:
        current_savings += monthly_saved/12 + current_savings*(annual_rate/12)
        num_months += 1
    return num_months


def main():
    annual_salary = float(input('Enter your annual salary: '))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = float(input('Enter the cost of your dream home: '))
    portion_down_payment = 0.25
    annual_rate = 0.04
    current_savings = 0
    num_months = months_to_save(
        total_cost, portion_down_payment, current_savings, 
        annual_rate, annual_salary, portion_saved
    )
    print(f'Number of months: {num_months}')


if __name__ == '__main__':
    main()

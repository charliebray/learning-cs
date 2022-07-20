def main():
    annual_salary = float(input('Enter your annual salary: '))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = float(input('Enter the cost of your dream home: '))
    semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))

    required_amount = total_cost * 0.25
    current_savings = 0

    num_months = 0
    while current_savings < required_amount:
        current_savings = current_savings * (1 + 0.04/12)
        current_savings += annual_salary * portion_saved / 12
        num_months += 1
        if num_months % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)

    print(f'Number of months: {num_months}')

if __name__ == '__main__':
    main()
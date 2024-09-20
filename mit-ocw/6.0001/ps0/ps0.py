import numpy as np

def power(base: int, exponent: int) -> float:
    """
    Calculate the base raised to the power of the exponent.

    Args:
        base (int): The base number.
        exponent (int): the exponent to raise the base to.

    Returns:
        float: The result of the base raised to the power of exponent.
    """
    return base ** exponent


def log_2(value: float) -> float:
    """
    Calculate logarithm base 2 of the given value.

    Args:
        value (float): A number to calculate log base 2 of.

    Returns:
        float: The log base 2 of the input value.

    Raises:
        ValueError: If the input value is non-positive.
    """
    if value <= 0:
        raise ValueError("Logarithm is undefined for non-positive values.")
    return np.log2(value)


def main() -> None:
    """
    Main function to take user input and display results of power and log base 2 calculations.

    Prompts the user to input 2 numbers, then prints:
    1. The result of the first number raised to the power of the second number.
    2. The log base 2 of the first number.

    Handles invalid input with error messages.
    """
    try:
        x = int(input('Enter number x: '))
        y = int(input('Enter number y: '))

        print(f'{x} raised to the power of {y} is: {power(x,y)}')
        print(f'Log base 2 of {x} is: {log_2(x)}')

    except ValueError:
        print("Invalid input. Please enter valid integers.")
    return None

if __name__ == '__main__':
    main()

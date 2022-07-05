class Fraction:
    '''
    Define a Fraction class.
    '''

    def __init__(self, top, bottom) -> None:

        '''
        Initialise fraction object with numerator and denominator attributes.
        '''

        # Check if top and bottom are integers, else raise an exception.
        if (type(top) != int) or (type(bottom) != int):
            if (type(top) != int) and (type(bottom) != int):
                raise RuntimeError(f'Both {top} and {bottom} are not integers. Only integers can be used.')
            elif type(top) != int:
                raise RuntimeError(f'{top} is not an integer. Only integers can be used.')
            elif type(bottom) != int:
                raise RuntimeError(f'{bottom} is not an integer. Only integers can be used.')

        # Ensure the denominator isn't negative (to ensure operations work correctly).
        if bottom < 0:
            top, bottom = int(-top), int(-bottom)

        # Determine GCD of the two integers.
        m, n = top, bottom
        while m % n != 0:
            m, n = n, m % n

        # Simplify fraction and define attributes.
        self.num = top // n
        self.den = bottom // n

    def __str__(self) -> str:

        '''
        Overwrite string method for printing.
        '''

        return f'{self.num}/{self.den}'

    def __repr__(self) -> str:
        
        '''
        Returns a printable representation of the object - one of the ways
        possible to create this object.
        '''

        return f'Fraction({self.num}, {self.den})'

    def get_num(self) -> str:

        '''
        Returns the numerator of the fraction.
        '''

        return f'{self.num}'

    def get_dem(self) -> str:

        '''
        Returns the denominator of the fraction
        '''

        return f'{self.den}'

    def __add__(self, another_frac):

        '''
        Addition of two fraction objects with result in simplified form.
        '''

        new_num = (self.num * another_frac.den) + (self.den * another_frac.num)
        new_den = self.den * another_frac.den

        return Fraction(new_num, new_den)

    def __radd__(self, another_frac):

        '''
        Reverse addition of two fraction objects.
        If __add__ fails, python naturally calls this method.
        '''

        new_num = (another_frac.num * self.num) + (another_frac.den * self.num)
        new_den = another_frac.den * self.den 

        return Fraction(new_num. new_den)

    def __iadd__(self, another_frac):

        '''
        Overwrite add to self.
        '''

        return self.__add__(another_frac)

    def __sub__(self, another_frac):

        '''
        Subtraction of two fraction objects with result in simplified form.
        '''

        return self.__add__(Fraction(int(-1 * another_frac.num), another_frac.den))

    def __mul__(self, another_frac):

        '''
        Multiplication of two fraction objects with result in simplified form.
        '''

        new_num = self.num * another_frac.num
        new_den = self.den * another_frac.den
        
        return Fraction(new_num, new_den)

    def __truediv__(self, another_frac):

        '''
        Division of two fraction objects with resullt in simplified form.
        '''

        return self.__mul__(Fraction(another_frac.den, another_frac.num))

    def __lt__(self, another_frac):

        '''
        Create a less than operator for Fraction objects.
        '''

        return (self.num * another_frac.den) < (self.den * another_frac.num)

    def __gt__(self, another_frac):

        '''
        Similiary, we define a greater than operator for Fraction objects.
        '''

        return another_frac.__lt__(self)

    def __le__(self, another_frac):

        '''
        Create a less than or equal to operator for Fraction objects.
        '''

        return (self.num * another_frac.den) <= (self.den * another_frac.num)

    def __ge__(self, another_frac):
        
        '''
        Create a greater than or equal to operator for Fraction objects.
        '''

        return (self.num * another_frac.den) >= (self.den * another_frac.num)

    def __eq__(self, another_frac):

        '''
        Overwrite equality to allow for deep equality.
        '''

        return (self.num * another_frac.den == self.den * another_frac.num)

    def __ne__(self, another_frac):

        '''
        Create a not-equal-to operator for Fraction objects.
        '''

        return not self.__eq__(another_frac)

def main():
    a_fraction = Fraction(1,2)
    b_fraction = Fraction(1,2)
    c_fraction = a_fraction + b_fraction
    print(c_fraction)
    print(repr(c_fraction))

main()

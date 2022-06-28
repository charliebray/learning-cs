'''
Helper function:
Determines the largest integer that divides m & n with a remainder of zero.
'''
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

'''
Define a Fraction class.
'''

class Fraction:

    def __init__(self, top, bottom) -> None:

        '''
        Initialise fraction object with numerator and denominator attributes.
        '''

        self.num = top
        self.den =  bottom

    def __str__(self) -> str:

        '''
        Overwrite string method for printing.
        '''

        return f'{self.num}/{self.den}'

    def __add__(self, another_frac):

        '''
        Addition of two fraction objects with result in simplified form.
        '''

        new_num = (self.num * another_frac.den) + (self.den * another_frac.num)
        new_den = self.den * another_frac.den
        gcd_int = gcd(new_num, new_den)
        new_num, new_den = int(new_num/gcd_int), int(new_den/gcd_int)

        return Fraction(new_num, new_den)

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
        gcd_int = gcd(new_num, new_den)
        new_num, new_den = int(new_num/gcd_int), int(new_den/gcd_int)
        
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

    def __eq__(self, another_frac):

        '''
        Overwrite equality to allow for deep equality.
        '''

        return (self.num * another_frac.den == self.den * another_frac.num)

def main():
    a_fraction = Fraction(3,4)
    b_fraction = Fraction(1,4)
    print(a_fraction < b_fraction)

main()

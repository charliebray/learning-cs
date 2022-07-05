class HalfAdder:
    '''
    Here we define a half adder.
    '''

    def __init__(self, input_A: int, input_B: int) -> None:
        self.input_A = input_A
        self.input_B = input_B
        self.sum = self.xor_gate()
        self.carry = self.and_gate()

    def __str__(self) -> str:
        return f'{{sum: {self.sum}, carry: {self.carry}}}'

    def xor_gate(self) -> int:
        if self.input_A == self.input_B:
            return 0
        else:
            return 1

    def and_gate(self) -> int:
        if self.input_A == 1 and self.input_B == 1:
            return 1
        else:
            return 0
            
def main():
    half_adder = HalfAdder(1, 1)
    print(half_adder)
    
main()



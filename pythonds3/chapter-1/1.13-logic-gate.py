class LogicGate:
    
    def __init__(self, lbl) -> None:
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label 

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, lbl) -> None:
        LogicGate.__init__(self, lbl)
        self.pin_a = None
        self.pin_b = None 

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input(f'Enter pin A input for gate {self.get_label()}: '))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input(f'Enter pin B input for gate {self.get_label()}: '))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source 
            else:
                raise RuntimeError(f'Error: NO EMPTY PINS on the gate {self.get_label()}')

class AndGate(BinaryGate):

    def __init__(self, lbl) -> None:
        BinaryGate.__init__(self, lbl)
    
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):

    def __init__(self, lbl) -> None:
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def __init__(self, lbl) -> None:
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):

    def __init__(self, lbl) -> None:
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a != b:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self, lbl) -> None:
        LogicGate.__init__(self, lbl)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input(f'Enter pin input for gate {self.get_label()}: '))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError(f'Error: NO EMPTY PINS on the gate {self.get_label()}')

class NotGate(UnaryGate):

    def __init__(self, lbl) -> None:
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        pin = self.get_pin()
        if pin == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate) -> None:
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

def main():
    g1 = XorGate("G1")
    g2 = AndGate("G2")
    binary_sum = g1.get_output()
    binary_carry = g2.get_output()
    print(f'Sum: {binary_sum}, Carry: {binary_carry}')

main()
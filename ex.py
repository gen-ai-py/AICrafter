class Operation:
    """Abstract operation class"""
    def execute(self, num1, num2):
        pass

class Add(Operation):
    def execute(self, num1, num2):
        return num1 + num2

class Subtract(Operation):
    def execute(self, num1, num2):
        return num1 - num2

class Multiply(Operation):
    def execute(self, num1, num2):
        return num1 * num2

class Divide(Operation):
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zer

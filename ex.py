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
            raise ValueError("Cannot divide by zero!")
        return num1 / num2

class OperationFactory:
    """Factory to create operation objects"""
    @staticmethod
    def get_operation(operator):
        if operator == '+':
            return Add()
        elif operator == '-':
            return Subtract()
        elif operator == '*':
            return Multiply()
        elif operator == '/':
            return Divide()
        else:
            raise ValueError(f"Invalid operator {operator}")

def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    operation = OperationFactory.get_operation(operator)
    result = operation.execute(num1, num2)
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()

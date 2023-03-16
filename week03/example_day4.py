class Calculator:
    def __init__(self, a, b):
        self.number1 = a
        self.number2 = b

    def plus(self):
        return self.number1 + self.number2
    
    def minus(self):
        return self.number1 - self.number2
    
    def multiply(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 // self.number2

    def print(self):
        print(f'# number1 = {self.number1}, number2 = {self.number2}')
        print(f'# 합 : {self.plus()}')
        print(f'# 빼기 : {self.minus()}')
        print(f'# 곱 : {self.multiply()}')
        print(f'# 몫 : {self.division()}')

# plus()
calculator = Calculator(10, 5)
print(f'# {calculator.plus()}')

calculator.number1 = -2
calculator.number2 = 2
print(f'# {calculator.plus()}')

# minus()
calculator = Calculator(10, 5)
print(f'# {calculator.minus()}')

calculator.number1 = -2
calculator.number2 = 2
print(f'# {calculator.minus()}')

# multiply()
ccalculator = Calculator(10, 5)
print(f'# {calculator.multiply()}')

calculator.number1 = -2
calculator.number2 = 2
print(f'# {calculator.multiply()}')

# division()
calculator = Calculator(10, 5)
print(f'# {calculator.division()}')

calculator.number1 = -2
calculator.number2 = 2
print(f'# {calculator.division()}')

# print()
calculator = Calculator(10, 5)
calculator.print()

calculator.number1 = -2
calculator.number2 = 2
calculator.print()
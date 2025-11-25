class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
print("-----Simple Calculator-----")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

calculator = Calculator()

add = calculator.add(num1, num2)
sub = calculator.subtract(num1, num2)
mul = calculator.multiply(num1, num2)
div = calculator.divide(num1, num2)

print(num1, "+", num2, "=", add)
print(num1, "-", num2, "=", sub)
print(num1, "*", num2, "=", mul)
print(num1, "/", num2, "=", div)
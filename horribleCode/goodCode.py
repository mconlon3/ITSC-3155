"""
Fixed Calculator (utilizes three principles):
1) KISS
2) DRY
3) Single Responsibility
"""
class Calculator:
    # KISS - all operations are simple
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 0
        return a / b

# Single Responsibility: this is the UI and all the calculator functions are in the Class.
calc = Calculator()
on = True
while(on):
    option = input("Choose operation (add/subtract/multiply/divide/off): ")
    if option == "off":
        print("Calculator powered off...")
        on = False
    # DRY: uses one elif for all the operations in order to reuse the input code
    elif option in ["add", "subtract", "multiply", "divide"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if option == "add":
            print(f"The result is {calc.add(a,b)}")
        elif option == "subtract":
            print(f"The result is {calc.subtract(a,b)}")
        elif option == "multiply":
            print(f"The result is {calc.multiply(a,b)}")
        elif option == "divide":
            print(f"The result is {calc.divide(a,b)}")
    else:
        print("Invalid option!")
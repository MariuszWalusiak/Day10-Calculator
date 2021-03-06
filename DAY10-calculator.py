# Calculator
from calculatorArt import logo

# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?"))

    for symbol in operations:
        print(symbol)
    continue_calculating = True

    while continue_calculating:
        operation_symbol = input("Pick an operation :")
        num2 = float(input("What is the  next number?"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to cotinue with {answer}, or type 'n' to start a new calculation:")

        if choice == "y":
            num1 = answer
        elif choice == "n":
            operation_symbol = False
            calculator()


calculator()

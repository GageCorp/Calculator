#Calculaor
from art import logo
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#divide
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
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_calculating = True
    while continue_calculating == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        selected_operation = operations[operation_symbol]
        answer = selected_operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            continue_calculating = False
            calculator()

calculator()
        
    

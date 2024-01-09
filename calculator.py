from calc_art import logo
print(logo)

#calculator
#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {"+":add,
              "-":substract,
              "*":multiply,
              "/":divide,
              }

def calculator():
    num1 = float(input("What's the first number?: "))
    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation (+ , - , * , / ): ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)   
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
                num1 = answer
        else:
            continue_calculation = False
            calculator()

calculator()
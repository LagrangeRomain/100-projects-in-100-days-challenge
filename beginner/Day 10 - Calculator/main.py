import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
first_number = None

while True:
    if first_number == None:
        first_number = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))
    result= calculator_dict[operation](first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")
    should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if should_continue == 'y':
        first_number = result
    else:
        first_number = None
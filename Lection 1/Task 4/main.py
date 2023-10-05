import math

def calculator():
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (sqrt)")
    print("6. Exponentiation (^)")

    choice = input("Enter the operation number (1/2/3/4/5/6): ")

    num1 = float(input("Enter the first number: "))

    if choice in ['1', '2', '3', '4', '6']:
        num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            result = "Error: division by zero"
            operation = '/'
    elif choice == '5':
        if num1 >= 0:
            result = math.sqrt(num1)
            operation = 'sqrt'
        else:
            result = "Error: taking square root of a negative number"
            operation = 'sqrt'
    elif choice == '6':
        result = num1 ** num2
        operation = '^'
    else:
        result = "Error: Invalid operation choice"
        operation = 'Error'

    print(f"Result: {num1} {operation} {num2} = {result}")

calculator()
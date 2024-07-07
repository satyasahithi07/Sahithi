# Simple Calculator

def calculator():
    # Prompt user to input first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt user to input second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt user to choose an operation
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        operation_symbol = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_symbol = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid input. Please choose a valid operation.")
        return
    
    # Display the result
    print(f"The result of {num1} {operation_symbol} {num2} is: {result}")

# Run the calculator
calculator()

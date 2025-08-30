# Task 2:  Calculator

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Returns the division of two numbers, handling division by zero."""
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

def main():
    """Main function to run the calculator application."""
    print("Simple Calculator")

    try:
        # Prompt the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Prompt for the operation choice
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter your choice (1/2/3/4): ")

    result = None
    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    if result is not None:
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()

# task2.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    while True:
        print("\nA Simple Calculator")
        print("Available operations are:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        operation = input("Choose an operation from 1 to 5: ")

        if operation == '5':
            print("Exiting the calculator. Adios!")
            break
        
        if operation in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            if operation == '1':
                result = add(num1, num2)
                op_symbol = "+"
            elif operation == '2':
                result = subtract(num1, num2)
                op_symbol = "-"
            elif operation == '3':
                result = multiply(num1, num2)
                op_symbol = "*"
            elif operation == '4':
                result = divide(num1, num2)
                op_symbol = "/"
            
            if isinstance(result, str):  # Check if result is an error message
                print(result)
            else:
                print(f"The result of {num1} {op_symbol} {num2} is: {result}")
        else:
            print("Invalid operation choice. Please choose a number between 1 and 5.")

if __name__ == '__main__':
    main()

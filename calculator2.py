def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Cannot divide by zero"
        result /= num
    return result

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num_count = int(input("Enter the number of values: "))
        numbers = []
        for i in range(num_count):
            num = float(input(f"Enter value {i + 1}: "))
            numbers.append(num)

        if user_input == "add":
            print("Result:", add(numbers))
        elif user_input == "subtract":
            print("Result:", subtract(numbers))
        elif user_input == "multiply":
            print("Result:", multiply(numbers))
        elif user_input == "divide":
            print("Result:", divide(numbers))
    else:
        print("Invalid input")

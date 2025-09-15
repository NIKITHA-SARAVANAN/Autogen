def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Test cases
print(calculate(10, 5, 'add'))         # Expected output: 15
print(calculate(10, 5, 'subtract'))    # Expected output: 5
print(calculate(10, 5, 'multiply'))    # Expected output: 50

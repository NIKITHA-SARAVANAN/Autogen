def add_numbers(num1, num2):
    return num1 + num2

# Test cases
test_cases = [
    (1, 2),    # Expected output: 3
    (-1, 1),   # Expected output: 0
    (100, 200) # Expected output: 300
]

# Checking results for the test cases
results = [add_numbers(num1, num2) for num1, num2 in test_cases]
results

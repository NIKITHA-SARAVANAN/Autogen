def add_numbers(a, b):
    return a + b

# Test cases
test_cases = [
    (3, 5),    # Test case 1: 3 + 5 = 8
    (-1, 1),   # Test case 2: -1 + 1 = 0
    (0, 0)     # Test case 3: 0 + 0 = 0
]

# Collect results
results = [add_numbers(a, b) for a, b in test_cases]
results

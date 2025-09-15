def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sort the left half
        merge_sort(right_half)  # Sort the right half

        i = j = k = 0
        
        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Test cases
test_case_1 = [38, 27, 43, 3, 9, 82, 10]
test_case_2 = [5, 2, 1, 3, 4]
test_case_3 = [-1, 0, -3, 5, 2, 1]

print(merge_sort(test_case_1))  # Expected output: [3, 9, 10, 27, 38, 43, 82]
print(merge_sort(test_case_2))  # Expected output: [1, 2, 3, 4, 5]
print(merge_sort(test_case_3))  # Expected output: [-3, -1, 0, 1, 2, 5]

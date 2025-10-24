def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1# Return -1 if not found


numbers = [5, 3, 7, 1, 9, 2]
target = int(input("Enter a number"))

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
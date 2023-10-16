def quick_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (in this case, the middle element)
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # Initialize lists for elements less than, equal to, and greater than the pivot
    left, equal, right = [], [], []

    # Divide the elements into the appropriate lists
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    # Recursively sort the left and right lists
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # Combine the sorted lists with the equal elements in the middle
    return sorted_left + equal + sorted_right


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)

    sorted_arr = quick_sort(arr)

    print("Sorted Array:", sorted_arr)

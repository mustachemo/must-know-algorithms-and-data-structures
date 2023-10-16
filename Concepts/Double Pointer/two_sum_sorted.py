def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        print("Array:", arr)
        print("Pointers:", " " * left + "^" + " " * (right - left - 1) + "^")
        print(f"Checking elements: {arr[left]} and {arr[right]}")

        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    target_sum = 9
    result = two_sum_sorted(sorted_array, target_sum)

    if result:
        print(f"Pair that sums up to {target_sum}: {result}")
    else:
        print("No such pair found.")

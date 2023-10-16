import time


def visualize_sliding_window(arr, k):

    # Step 1: Initialize the variables
    n = len(arr)
    max_sum = float("-inf")
    current_sum = sum(arr[:k])
    left = 0
    right = k - 1

    while right < n:
        # Print the array
        print("Array:", arr)
        print("Sliding Window:", arr[left:right + 1])
        print(f"Current Sum: {current_sum} (Max Sum: {max_sum})")
        print("-" * 40)

        # Update the max sum
        max_sum = max(max_sum, current_sum)

        # Move the window
        right += 1
        if right < n:  # Check if right is still within the array bounds
            current_sum += arr[right]  # Add the rightmost element
        if left <= right and left < n:  # Check if left is still within the array bounds
            current_sum -= arr[left]  # Remove the leftmost element
            left += 1  # Slide the window to the right

        time.sleep(1)  # Pause for 1 second to visualize

    # Display the final result
    print("Final Maximum Sum:", max_sum)


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    visualize_sliding_window(arr, k)

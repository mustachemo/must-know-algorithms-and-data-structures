def remove_duplicates(nums):
    if not nums:
        return 0

    # Initialize two pointers
    left = 0

    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]

        print("Array:", nums)
        print("Left Pointer:", left)
        print("Right Pointer:", right)
        print("-" * 40)

    return left + 1


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    new_length = remove_duplicates(nums)
    print("New Length:", new_length)
    print("Updated Array:", nums[:new_length])

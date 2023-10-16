# is unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def check_string_uniqueness(string) -> bool:
    '''Big O: O(n^2)'''

    for index, char in enumerate(string):
        for index2, char2 in enumerate(string):
            if char == char2 and index != index2:
                return False
    return True


def check_string_uniqueness_optimized(string) -> bool:
    '''Big O: O(n)'''

    left_ptr, right_ptr = (0, 0)
    n = len(string)

    while left_ptr != n:
        if left_ptr != right_ptr and string[left_ptr] == string[right_ptr]:
            return False

        if right_ptr == n - 1:
            right_ptr = 0
            left_ptr += 1

        right_ptr += 1

    return True


if __name__ == "__main__":
    string_example1 = "hello"
    string_example2 = "sophia"
    string_example3 = "abcdefg"
    string_example4 = "apple"
    string_example5 = ""

    print("Using brute force:")
    print(check_string_uniqueness(string_example1))  # False (repeated 'l')
    print(check_string_uniqueness(string_example2))  # True
    print(check_string_uniqueness(string_example3))  # True
    print(check_string_uniqueness(string_example4))  # False (repeated 'p')
    print(check_string_uniqueness(string_example5))  # True (empty string)

    print("Using optimized solution:")
    print(check_string_uniqueness_optimized(
        string_example1))  # False (repeated 'l')
    print(check_string_uniqueness_optimized(string_example2))  # True
    print(check_string_uniqueness_optimized(string_example3))  # True
    print(check_string_uniqueness_optimized(
        string_example4))  # False (repeated 'p')
    print(check_string_uniqueness_optimized(
        string_example5))  # True (empty string)

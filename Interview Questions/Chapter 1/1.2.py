# check permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(string1: str, string2: str) -> bool:
    n1 = len(string1)
    permutation_check = 0

    for index, char in enumerate(string1):
        for index2, char2 in enumerate(string2):
            if char2 == char:
                permutation_check += 1
        if permutation_check == n1:
            return True
    return False


if __name__ == "__main__":
    string1 = "abc"
    string2 = "bca"
    string3 = "abcd"
    string4 = "abcc"
    string5 = "abcdef"
    string6 = "xyz"

    # Test cases where one string is a permutation of the other
    # True (string2 is a permutation of string1)
    print(check_permutation(string1, string2))
    # True (a string is always a permutation of itself)
    print(check_permutation(string1, string1))

    # Test cases where one string is not a permutation of the other
    print(check_permutation(string1, string3))  # False (different lengths)
    print(check_permutation(string1, string4))  # False (string4 has extra 'c')
    print(check_permutation(string1, string5))  # False (different lengths)
    # False (completely different characters)
    print(check_permutation(string1, string6))

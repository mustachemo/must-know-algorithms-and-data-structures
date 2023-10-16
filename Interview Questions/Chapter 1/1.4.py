# palindrome permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.

def palindrome_permutation(string: str) -> bool:
    modified_string = string.replace(' ', '')
    n = len(modified_string) - 1

    for i in range(n):
        if modified_string[i] != modified_string[n]:
            return False
        n -= 1

    return True


if __name__ == "__main__":
    # Write me test cases
    example1 = "taco cat"
    example2 = "racecar"
    example3 = "hello world"

    print(palindrome_permutation(example1))  # Should return True
    print(palindrome_permutation(example2))  # Should return True
    print(palindrome_permutation(example3))  # Should return False

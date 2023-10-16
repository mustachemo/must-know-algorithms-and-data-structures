# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true" length of the string.

def URLify(string: str) -> str:
    modified_string = ""

    for char in string:
        if char == ' ':
            modified_string += '%20'
        else:
            modified_string += char

    return modified_string

    # modified_string = string.replace(' ', '%20')
    # return modified_string

    return string


if __name__ == "__main__":
    # Test cases with spaces to be replaced
    input_str1 = "Hello, World!"
    input_str2 = "This is a test."
    input_str3 = "  Spaces  in   between  words  "

    # Expected output after URLify
    expected_output1 = "Hello,%20World!"
    expected_output2 = "This%20is%20a%20test."
    expected_output3 = "%20%20Spaces%20%20in%20%20%20between%20%20words%20%20"

    URLify(input_str1) == expected_output1

    # Test cases where spaces are replaced with "%20"
    assert URLify(input_str1) == expected_output1
    assert URLify(input_str2) == expected_output2
    assert URLify(input_str3) == expected_output3

    # Test cases with no spaces
    input_str4 = "NoSpacesHere"
    input_str5 = ""

    # Expected output should be the same as input when there are no spaces
    assert URLify(input_str4) == input_str4
    assert URLify(input_str5) == input_str5

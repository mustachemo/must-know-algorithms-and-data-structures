def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)

    return occurrences


# Example usage:
if __name__ == "__main__":
    text = "ABCABCABABCABABABC"
    pattern = "AB"

    matches = brute_force_string_match(text, pattern)

    if matches:
        print(f"Pattern found at positions: {matches}")
    else:
        print("Pattern not found.")

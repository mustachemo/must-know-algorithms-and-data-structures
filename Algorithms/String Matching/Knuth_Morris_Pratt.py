def build_kmp_table(pattern):
    m = len(pattern)
    kmp_table = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = kmp_table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        kmp_table[i] = j

    return kmp_table


def kmp_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    kmp_table = build_kmp_table(pattern)
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = kmp_table[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            occurrences.append(i - m + 1)
            j = kmp_table[j - 1]

    return occurrences


# Example usage:
if __name__ == "__main__":
    text = "ABCABCABABCABABABC"
    pattern = "AB"

    matches = kmp_string_match(text, pattern)

    if matches:
        print(f"Pattern found at positions: {matches}")
    else:
        print("Pattern not found.")

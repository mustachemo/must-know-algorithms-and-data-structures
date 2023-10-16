def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    # Create a 2D array to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    text1 = "ABCD"
    text2 = "ACDF"
    result = longest_common_subsequence(text1, text2)
    print(f"Length of the Longest Common Subsequence: {result}")

def solution(m, n, puddles):
    mod = 1_000_000_007
    dp = [[0] * 101 for _ in range(101)]

    for i, j in puddles:
        dp[i][j] = -1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif dp[i][j] == -1:
                continue
            else:
                dp[i][j] = (max(dp[i-1][j], 0) + max(dp[i][j-1], 0)) % mod

    return dp[m][n]

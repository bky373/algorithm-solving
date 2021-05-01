n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    if i <= 3:
        dp[i] = 1
    else:
        min_num = dp[i - 1]
        if i % 3 == 0:
            min_num = min(min_num, dp[i // 3])
        if i % 2 == 0:
            min_num = min(min_num, dp[i // 2])
        dp[i] = min_num + 1

print(dp[n])

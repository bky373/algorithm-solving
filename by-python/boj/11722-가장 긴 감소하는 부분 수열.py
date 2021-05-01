MAX = 1000

N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * (MAX + 1)

for i in range(N):
    for j in range(i):
        if numbers[j] > numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) + 1)

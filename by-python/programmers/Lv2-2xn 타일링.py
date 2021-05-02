def solution(n):
    mod = 1_000_000_007

    dp = [1, 1]

    for i in range(2, n + 1):
        dp.append((dp[-2] + dp[-1]) % mod)

    return dp[n]


if __name__ == '__main__':
    n = 4
    print(solution(n))

def largest_sum(arr):
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(dp)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(largest_sum(arr))

def solve(y, x):
    if y == n: return 0
    if dp[y][x] != -1: return dp[y][x]

    dp[y][x] = 0
    dp[y][x] = arr[y][x] + max(solve(y + 1, x), solve(y + 1, x + 1))
    return dp[y][x]


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(n)]

    print(solve(0, 0))

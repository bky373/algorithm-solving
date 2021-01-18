def dp(y, x):
    if y == n - 1 and x == n - 1: return 1
    if y >= n or x >= n: return 0

    if memo[y][x] != -1: return memo[y][x]  # arr과 동일한 좌표의 memo 값이 -1이 아니면 이미 지나쳐감
    memo[y][x] = 0

    jump = arr[y][x]
    memo[y][x] += dp(y + jump, x)
    memo[y][x] += dp(y, x + jump)
    return memo[y][x]


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    memo = [[-1] * (n + 1) for _ in range(n + 1)]

    print(dp(0, 0))

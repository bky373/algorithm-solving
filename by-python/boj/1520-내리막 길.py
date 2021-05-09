# dfs + dp
# 참고 : https://simsimjae.tistory.com/23
import sys

sys.setrecursionlimit(10 ** 9) # 런타임에러 방지
input = sys.stdin.readline


def dfs(y, x):
    if dp[y][x] != -1: return dp[y][x]
    if y == 0 and x == 0: return 1

    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= m or nx < 0 or nx >= n: continue

        if arr[ny][nx] > arr[y][x]:
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]


def main():
    print(dfs(m - 1, n - 1))


if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    main()

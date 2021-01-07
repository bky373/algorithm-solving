import sys

input = sys.stdin.readline


# 방법 1
# 단순 구현
# 시간 복잡도 O(NM)
# PyPy는 통과, Python3는 시간 초과
def solution(i, j, x, y):
    total = 0
    for r in range(i, x + 1):
        total += sum(arr[r][j:y + 1])
    return total


# 방법 2
# Python3까지도 매우 빠르게 통과
# 메모이제이션으로 복잡도가 확 줄었다
# S[i] = S[i-1] + A[i]
# A[i]..A[j]의 합 = S[j] - S[i-1]
def solution_2(i, j, x, y):
    total = 0
    for r in range(i, x + 1):
        total += dp[r][y] - dp[r][j - 1]
    return total


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        arr[i] = [0] + list(map(int, input().split()))

        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1] + arr[i][j]

    k = int(input())

    for _ in range(k):
        i, j, x, y = map(int, input().split())
        # print(solution(i, j, x, y))
        print(solution_2(i, j, x, y))

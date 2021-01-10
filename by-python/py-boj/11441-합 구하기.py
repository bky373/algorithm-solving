# 표준 입력이 아니라면 실패..
import sys

input = sys.stdin.readline


def main():
    n, arr = int(input()), list(map(int, input().split()))
    S = [0] * (n + 1)
    for i in range(1, n + 1):
        S[i] = S[i - 1] + arr[i - 1]

    m = int(input())
    for _ in range(m):
        i, j = map(int, input().split())
        print(S[j] - S[i - 1])


if __name__ == '__main__':
    main()

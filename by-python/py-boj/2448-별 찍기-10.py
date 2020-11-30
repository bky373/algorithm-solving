import sys

sys.setrecursionlimit(1000000000)

n = int(input())
arr = [[' '] * n for _ in range(n)]


def solve(y, x, n):
    if n == 1:
        arr[y][x] = '*'
        return

    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                solve(y + (i * div), x + (j * div), div)


def show_stars(arr):
    for a in arr:
        print(''.join([c for c in a]))


solve(0, 0, n)
show_stars(arr)

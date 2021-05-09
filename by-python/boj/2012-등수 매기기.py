import sys

input = sys.stdin.readline


def solve(data):
    data.sort()
    result = 0
    for k in range(n):
        result += abs(data[k] - k - 1)
    return result


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(int(input()))

    print(solve(data))

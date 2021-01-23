def solve(n, k):
    arr = list(map(str, range(1, n + 1)))
    ans = '<'
    idx = 0
    while len(arr) > 1:
        out = (idx + k - 1) % len(arr)
        ans += arr[out] + ', '
        del arr[out]
        idx = out
    ans += arr[0] + '>'
    return ans


if __name__ == '__main__':
    n, k = map(int, input().split())

    print(solve(n, k))

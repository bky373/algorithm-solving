def binary_search(heights, m):
    lo, hi = 0, max(heights)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        tot = 0
        for h in heights:
            tot += (h - mid) if h > mid else 0
        if tot >= m:
            lo = mid
        else:
            hi = mid
    print(lo)


if __name__ == '__main__':
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    binary_search(heights, m)

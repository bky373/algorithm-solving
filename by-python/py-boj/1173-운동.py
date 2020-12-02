def solve(N, m, M, T, R):
    exercise, amount = 0, 0
    x = m
    if m + T > M:
        return -1

    while True:
        if exercise == N:
            return amount
        if x + T <= M:
            exercise += 1
            x += T
        else:
            x -= R
            if m > x:
                x = m
        amount += 1


if __name__ == '__main__':
    N, m, M, T, R = map(int, input().split())
    print(solve(N, m, M, T, R))

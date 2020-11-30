def solve(paid, mymoney):
    coins = [500, 100, 50, 10, 5, 1]
    cnt = 0
    v = mymoney - paid
    i = 0
    while v > 0:
        if v >= coins[i]:
            v -= coins[i]
            cnt += 1
        else:
            i += 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    print(solve(n, 1000))

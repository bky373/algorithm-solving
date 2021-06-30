def solution():
    N = input()
    zero_cnt = N.count('0')

    N = N.replace('0', '')
    N = list(N)
    N.sort(reverse=True)

    if zero_cnt == 0:
        return -1

    N = int(''.join(N))

    if N % 3 == 0:
        return N * (10 ** zero_cnt)

    return -1


if __name__ == '__main__':
    print(solution())

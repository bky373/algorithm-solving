def factorizate(n):
    for i in range(2, int(n ** .5) + 1):
        while n % i == 0:
            print(i)
            n //= i

    if n > 1:
        print(n)


if __name__ == '__main__':
    n = int(input())
    factorizate(n)

def gcd(a, b):
    return a if not b else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        A, B = map(int, input().split())
        print(lcm(A, B))

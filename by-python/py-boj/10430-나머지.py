def solution(a, b, c):
    return [(a + b) % c, ((a % c) + (b % c)) % c, (a * b) % c, ((a % c) * (b % c)) % c]


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print('\n'.join([str(n) for n in solution(a, b, c)]))

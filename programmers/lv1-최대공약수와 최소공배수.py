""" 1번: 나의 풀이 """
def gcd(a, b):
    gcm = 1
    for k in range(2, min(a, b) + 1):
        while a % k == 0 and b % k == 0:
            a //= k
            b //= k
            gcm *= k

    return gcm

def lcm(a, b):
    return a*b//gcd(a, b)

def solution(n, m):
    g = gcd(n, m)
    return [g, lcm(n, m, g)]




""" 2번: 다른 사람의 풀이 """
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return [c, a*b//c]


def solution(n, m):
    return gcdlcm(n, m)



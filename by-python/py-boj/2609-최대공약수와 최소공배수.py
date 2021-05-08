a, b = map(int, input().split())

t = 1
c, d = max(a, b), min(a, b)
while t > 0:
    t = c % d
    c, d = d, t

print(c, a*b//c)

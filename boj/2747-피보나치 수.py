""" 1. 내가 작성한 코드 (DP를 이용-1) """
x = int(input())
if x <= 1:
    print(x)
    exit(0)

if x > 1:
    cache = [0] * (x+1)
    cache[0] = 0
    cache[1] = 1
    for x in range(2, x+1):
        cache[x] = cache[x-1] + cache[x-2] 
print(cache[x])


""" 2. 1번 통과 후 참고한 코드 (DP를 이용-2) """
n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)

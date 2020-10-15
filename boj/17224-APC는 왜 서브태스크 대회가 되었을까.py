""" 1번: 내가 작성한 코드 (sorted 이용) """
n, l, k = map(int, input().split())

problems = []

for _ in range(n):
    easy, hard = map(int, input().split())
    problems.append((easy, hard))

problems = sorted(problems, key=lambda x: x[1])

solved = 0
total = 0

for problem in problems:
    if solved >= k :
        break
    if problem[0] <= l:
        total += 100
        if problem[1] <= l:
            total += 40
        solved += 1
print(total)




""" 2번: 1번 성공 후 참고한 코드 """
N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K) * 140

if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)

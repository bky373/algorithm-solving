N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    student[Y-1][S] += 1
    
cnt = 0
for s in student:
    if s[0] != 0:
        cnt += 1
    while s[0] > K:
        cnt += 1
        s[0] -= K
    
    if s[1] != 0:
        cnt += 1
    while s[1] > K:
        cnt += 1
        s[1] -= K
print(cnt)

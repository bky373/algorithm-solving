n, s, m = map(int, input().split())
songs = list(map(int, input().split()))

v = [[False for _ in range(m+1)] for _ in range(n+1)]
v[0][s] = True

for i in range(1, n+1):
    for j in range(m+1):
        if v[i-1][j] == True:
            if 0 <= j - songs[i-1]:
                v[i][j - songs[i-1]] = True
            if j + songs[i-1] <= m:
                v[i][j + songs[i-1]] = True

ans = -1
for i in range(m, -1, -1):
    if v[n][i] == True:
        ans = i
        break

print(ans)

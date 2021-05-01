R, C = map(int, input().split())
M = [list(input()) for i in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
is_sheep = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx < 0 or nx == R or ny < 0 or ny == C:
                    continue
                if M[nx][ny] == 'S':
                    is_sheep = True

if is_sheep:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'
    for i in M:
        print(''.join(i))

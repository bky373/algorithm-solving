def new_arr(N):
    return [[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())
B = [list(input()) for _ in range(N)]
visit = new_arr(N) 
visit2 = new_arr(N) 

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    visit[x][y] = True
    result = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if visit[xx][yy] or B[x][y] != B[xx][yy]:
            continue
        result += dfs(xx, yy)
    return result

def dfs2(x, y, val):
    visit2[x][y] = True
    B[x][y] = '0'
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if visit2[xx][yy] or B[xx][yy] != val:
            continue
        dfs2(xx, yy, val)

def downward():
    for i in range(10):
        tmp = []
        for j in range(N):
            if B[j][i] != '0':
                tmp.append(B[j][i])

        for j in range(N-len(tmp)):
            B[j][i] = '0'

        for j in range(N-len(tmp), N):
            B[j][i] = tmp[j-N+len(tmp)]

while True:
    existed = False
    visit = new_arr(N)
    visit2 = new_arr(N)
    for i in range(N):
        for j in range(10):
            if B[i][j] == '0' or visit[i][j]:
                continue
            result = dfs(i, j) # 개수 세기
            if result >= K:
                dfs2(i, j, B[i][j]) # 지우기
                existed = True
    if not existed:
        break
    downward() # 내리기

for i in B:
    print(''.join(i))

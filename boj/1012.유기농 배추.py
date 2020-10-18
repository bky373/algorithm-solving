""" 1번: 내가 작성한 코드(큐 활용) """
T = int(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def BFS(i, j):
    queue = [(i, j)]
    while queue:
        cur = queue.pop(0)
        i, j = cur[0], cur[1]
        for w in range(4):
            ii, jj = i+dx[w], j+dy[w]
            if ii < 0 or ii == N or jj < 0 or jj == M:
                continue
            if not visited[ii][jj] and G[ii][jj]:
                visited[ii][jj] = 1
                queue.append((ii, jj))


for _ in range(T):
    M, N, K = map(int, input().split())
    G = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        G[y][x] = 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = 1
                if G[i][j]:
                    cnt += 1
                    BFS(i,j)
    print(cnt)


""" 2번: 1번 성공 후 참고한 코드(dfs 활용) """
import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0 , -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        # 배추가 없거나 이미 방문했으면 넘어간다
        if B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx, yy)

def process():
    global B, ck

    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j]:
                continue
            dfs(i,j)
            ans += 1
    print(ans)

for _ in range(T):
    process()

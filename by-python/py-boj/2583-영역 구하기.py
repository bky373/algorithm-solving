import sys

sys.setrecursionlimit(100000000)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def visit(x, y, cnt):
    board[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= m or 0 > ny or ny >= n:
            continue
        if board[nx][ny]:
            continue
        cnt = visit(nx, ny, cnt)
    return cnt


if __name__ == '__main__':
    m, n, k = map(int, input().split())
    board = [[0] * n for _ in range(m)]

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())

        for i in range(x1, x2):
            for j in range(y1, y2):
                board[j][i] = 1

    result = 0
    area = []
    for i in range(m):
        for j in range(n):
            if not board[i][j]:
                result += 1
                area.append(visit(i, j, 0))

    print(result)
    print(' '.join([str(a) for a in sorted(area)]))

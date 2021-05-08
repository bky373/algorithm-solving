def bfs(y, x):
    global result

    q = set()
    q.add((y, x, arr[y][x]))

    while q:
        cy, cx, words = q.pop()
        result = max(result, len(words))

        # 한 단계씩 점진적 진행 : C에서 CA, CA -> CAD, CAD ...
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= r or nx < 0 or nx >= c: continue
            if arr[ny][nx] in words: continue
            q.add((ny, nx, words + arr[ny][nx]))


if __name__ == '__main__':
    r, c = map(int, input().split())
    arr = [input() for _ in range(r)]

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    result = 0
    bfs(0, 0)
    print(result)

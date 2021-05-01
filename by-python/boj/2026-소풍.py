def dfs(now, count):
    global existed
    if existed: return

    # 기저 사례: k명을 찾으면 종료한다
    if count == k:
        existed = True
        for x in range(len(visited)):
            if visited[x]:
                print(x)
        return

    # 이미 선택된 학생들과 친구이면서 아직 선택되지 않은 경우 재귀 돌림
    for next in range(now + 1, n + 1):
        if not visited[next] and has_relations(next):
            visited[next] = True
            dfs(next, count + 1)
            visited[next] = False


def has_relations(new):
    for x in range(len(visited)):
        if visited[x]:
            if not relations[new][x]:
                return False
    return True


if __name__ == '__main__':
    k, n, f = map(int, input().split())
    relations = [[False] * (n + 1) for _ in range(n + 1)]

    for _ in range(f):
        a, b = map(int, input().split())
        # 친구 관계 설정
        relations[a][b] = True
        relations[b][a] = True

    visited = [False for _ in range(n + 1)]
    existed = False
    count = 1

    # 오름차순으로 소풍인원 탐색
    for i in range(1, n + 1):
        if existed: break

        visited[i] = True
        dfs(i, count)
        visited[i] = False

    if not existed:
        print(-1)

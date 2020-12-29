import sys

input = sys.stdin.readline


def tsp(now, depth):
    global cur_len, result

    # 기저 사례: 모든 도시를 다 방문하면 시작 도시로 돌아가고 종료한다
    if depth == n:
        if dist[now][0] > 0:
            result = min(result, cur_len + dist[now][0])
        return

    visited[now] = 1

    # 나머지 도시들을 전부 방문해보도록 재귀 함수를 호출한다
    for next in link[now]:
        if visited[next]: continue

        cur_len += dist[now][next]
        tsp(next, depth + 1)
        cur_len -= dist[now][next]
    visited[now] = 0


if __name__ == '__main__':
    n = int(input())
    dist = [list(map(int, input().split())) for _ in range(n)]  # 두 도시간 거리 입력 받기
    visited = [0] * n
    link = {}
    cur_len, result = 0, 1e9

    for i in range(n):
        link[i] = []
        for j in range(n):
            if dist[i][j] > 0:
                link[i].append(j)

tsp(0, 1)

print(result)

# 참고 1) 책 < 프로그래밍 대회에서 배우는 알고리즘 문제해결전략 > (구종만 저)
# 참고 2) https://suri78.tistory.com/152

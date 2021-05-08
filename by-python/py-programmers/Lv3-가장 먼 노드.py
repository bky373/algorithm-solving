from collections import deque


def make_graph(n, edge):
    adjacents = [[] for _ in range(n + 1)]
    for (a_node, b_node) in edge:
        adjacents[a_node].append(b_node)
        adjacents[b_node].append(a_node)
    return adjacents


def bfs(start, graph, tour, steps):
    queue = deque([start])
    tour[start] = 1

    while queue:
        now = queue.popleft()

        for neighbor in graph[now]:
            if not tour[neighbor]:
                tour[neighbor] = 1
                steps[neighbor] = steps[now] + 1
                queue.append(neighbor)
    return steps


def count_longest(steps):
    max_val = max(steps)
    cnt = 0
    for step in steps:
        if step == max_val:
            cnt += 1
    return cnt


def solution(n, edge):
    graph = make_graph(n, edge)
    tour = [0] * (n + 1)
    steps = [0] * (n + 1)

    bfs(1, graph, tour, steps)
    return count_longest(steps)


if __name__ == '__main__':
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    result = solution(n, edge)
    print(result)

'''
# 프로그래머스 - Lv3 가장 먼 노드

## 1. 문제

> https://programmers.co.kr/learn/courses/30/lessons/49189

## 2. 고려할 점

-  1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 한다.

- 각 노드는 1부터 n까지 번호가 적혀있다. 

- 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.

- 노드의 개수 n은 2 이상 20,000 이하이다.

- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있다.

- vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미이다.

  ##### 입출력 예

  | n    | vertex                                                   | return |
  | ---- | -------------------------------------------------------- | ------ |
  | 6    | [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] | 3      |

## 3. 풀이

- 가중치가 없는 최단 경로를 계산하기 위해 BFS 방식을 사용하였다.
- 각 노드들을 돌 때, 다음 노드의 거리는 현재 노드의 거리 + 1로 계산해주었다.
- BFS가 끝나면 가장 긴 거리 값을 구하고, 이에 해당하는 노드가 몇 개 있는지 계산해준다.

## 4. 풀이 코드

- 위의 코드 참고

## 5. 주의할 점

- 가중치가 있다면 추가적인 조건을 고려해봐야 한다. 가중치가 양수일 경우 다익스트라 방법을 사용할 수 있다.

## 6. 배운 점

- 그래프를 그릴 때 딕셔너리를 사용하지 않고 이중 배열을 사용할 수 있다.
- 인접한 노드를 표현할 때 `next`를 주로  사용했는데 `neighbor`도 괜찮은 것 같다.
'''

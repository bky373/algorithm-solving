def make_graph(tickets):
    adjacents = {}
    for from_port, to_port in tickets:
        adjacents[from_port] = adjacents.get(from_port, []) + [to_port]
    return adjacents


def dfs(now, ticket_graph, result):
    if ticket_graph.get(now):
        for i in range(len(ticket_graph[now])):
            while ticket_graph[now]:
                next = ticket_graph[now][i]
                ticket_graph[now].remove(next)
                dfs(next, ticket_graph, result)
    result.append(now)
    return result


def solution(tickets):
    tickets.sort()
    start = "ICN"
    ticket_graph = make_graph(tickets)
    result = dfs(start, ticket_graph, [])
    return result[::-1]


if __name__ == '__main__':
    tickets = [["ICN", "ABC"], ["JFK", "ICN"], ["ICN", "JFK"], ["ABC", "DEF"], ["DEF", "ABC"]]
    print(solution(tickets))

'''
- 문제: https://programmers.co.kr/learn/courses/30/lessons/43164
- 풀이: 
    # 고려할 사항
    - 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
    - 주어진 공항 수는 3개 이상 10,000개 이하입니다.
    - tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
    - 주어진 항공권은 모두 사용해야 합니다.
    - 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
    - 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
    - 항상 "ICN" 공항에서 출발합니다.
    
    # 풀이
    - 알파벳 순으로 방문하기 위해 인수를 미리 정렬한다. 
    - 그 이후 인수를 인접 리스트 그래프로 만든다. 
        - 인수로 주어진 리스트를 그대로 사용할 수도 있다. 이때에는 특정 공항을 찾기 위해 반복문 + 조건문을 사용한다.
        - 나의 경우 이름을 찾는 반복문을 피하기 위해 인접 리스트를 사용하였고, 
            출발지 공항의 이름을 키로, 도착지 공항의 이름을 값으로 사용하였다. 
    - ICN 부터 DFS 방식으로 인접 리스트의 요소들을 방문한다.
        - DFS는 그래프 상에서 두 정점 사이의 경로가 있는지 확인할 수 있다. 
        - 어떤 정점 v에 대해 dfs(v)를 하면, v에서부터 간선을 통해 이동할 수 있는 모든 정점을 방문하게 된다.
        - 특히 모든 간선을 정확히 한 번씩 지나는 경우 dfs를 활용하여 문제를 해결할 수 있다.
    - 이 문제에서 어려운 부분은 정점을 다 돌기 전에 간선이 끊겨 경로가 중간에 종료될 수 있다는 점이다.
        - 해결 방법은 각 간선을 따라가는 순간에 경로를 추가하지 않고, 재귀 호출이 끝나고 반환되기 전 경로를 추가하는 것이다.
        - 따라서 경로의 끝점부터 역순으로 정점이 추가되므로 결과적으로 마지막엔 경로를 한 번 뒤집어주어야 한다.
        - 좀 더 이해를 돕자면, 
            만약 어떤 정점에서 아직 따라가지 않은 간선이 있을 때, 경로에는 지금까지 찾은 경로의 뒷부분(역순시)만이 저장되어 있다.
        - 이때 새 경로를 찾더라도 경로 중간에 끼워 주지 않는다. 대신 지금까지 만든 부분의 맨 뒤에 새 경로를 붙이고 나머지 부분을 계속 이어붙여준다.
'''

from collections import deque

MX = 100001
s, d = map(int, input().split())
array = [0] * MX

def bfs():
    q = deque([s])
    while q:
        cur_pos = q.popleft()
        if cur_pos == d:
            return array[cur_pos]
        for next_pos in (cur_pos - 1, cur_pos +1, cur_pos*2):
            if 0 <= next_pos < MX and not array[next_pos]:
                array[next_pos] = array[cur_pos] + 1
                q.append(next_pos)

print(bfs())

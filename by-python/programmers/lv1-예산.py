""" 1번: 나의 풀이 """
def solution(d, budget):
    d.sort()
    cnt = 0
    for i in range(1, len(d)+1):
        if sum(d[:i]) > budget:
            return cnt
        cnt += 1
    return cnt




""" 2번: 다른 사람의 풀이 """
def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

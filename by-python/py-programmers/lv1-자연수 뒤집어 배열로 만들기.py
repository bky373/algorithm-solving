""" 1번: 나의 풀이 """
def solution(n):
    return list(map(int, list(str(n))[::-1]))

    
    
    
""" 2번: 다른 사람의 풀이 (reversed 사용) """
def solution2(n):
    return list(map(int, reversed(str(n))))

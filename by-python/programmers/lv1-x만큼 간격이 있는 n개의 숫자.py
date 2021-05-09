""" 1번: 나의 풀이(map 사용) """
def solution(x, n):
    tmp = [i+1 for i in range(n)]
    return list(map(lambda t: t*x, tmp))

    


""" 2번: 다른 사람의 풀이 """
def solution2(x, n):
    return [x*(i+1) for i in range(n)]

def solution3(x, n):
    return [ i for i in range(x, x*n+1, x)]
def solution(n):
    sq = int(n**0.5)
    return int((sq+1)*(sq+1)) if sq*sq == n else -1

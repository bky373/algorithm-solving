def solution(n):
    return ''.join(map(str, sorted([int(x) for x in str(n)], reverse=True)))
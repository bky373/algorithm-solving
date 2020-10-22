def solution(n):
    tmp = ''
    while n > 0:
        a, b = divmod(n, 3)
        n = a
        tmp += str(b)   
    
    return sum([int(n)*(3**(len(tmp)-i-1)) for i, n in enumerate(tmp)])

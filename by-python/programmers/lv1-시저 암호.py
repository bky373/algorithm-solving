def solution(s, n):
    uppers = [ s for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    lowers = [ s for s in 'abcdefghijklmnopqrstuvwxyz']
    ans = ''
    for x in s:
        if x == ' ':
            ans += ' '
        else:
            if x.isupper():
                ans += uppers[(uppers.index(x)+n)%26] 
            else:
                ans += lowers[(lowers.index(x)+n)%26]
    return ans

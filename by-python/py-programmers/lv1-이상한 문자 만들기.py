""" 1번: 나의 풀이 """
def solution(s):
    ans = ''
    ck = False
    for x in range(len(s)):
        if s[x] == ' ':
            ans += ' '
            ck = True
            k = x + 1
        else:
            if ck:
                if (x-k) % 2:
                    ans += s[x].lower()
                    continue
            else:
                if x % 2:
                    ans += s[x].lower()
                    continue
            ans += s[x].upper()
    return ans



""" 2번: 1번 성공 후 참고한 풀이 """
def solution2(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])
    
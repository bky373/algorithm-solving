""" 1번: 나의 풀이 """
def solution(n):
    ans = 1
    k = n
    if n == 0:
        return 0
    while k > 1:
        if n % k == 0:
            ans += k
        k -= 1
    return ans



""" 2번: 1번 성공 후 참고한 풀이 """
def solution2(num):
    return 
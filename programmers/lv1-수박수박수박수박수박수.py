""" 1번: 나의 풀이 """
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2:
            answer += '박'
        else:
            answer += '수'
    return answer


""" 2번: 1번 성공 후 참고한 풀이 """
def solution2(n):
    s = '수박' * n
    return s[:n]

    
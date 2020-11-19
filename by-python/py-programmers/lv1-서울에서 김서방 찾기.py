""" 1번: 나의 풀이 """
def solution(seoul):
    return '김서방은 ' + str(seoul.index("Kim")) + '에 있다'



""" 2번: 1번 성공 후 참고한 풀이 """
def solution2(seoul):
    return '김서방은 {}에 있다'.format(seoul.index("Kim"))

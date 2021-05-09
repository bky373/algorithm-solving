""" 1번: 나의 풀이(count 사용) """
def solution(s):
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    
    if p == y:
        return True
    else:
        return False

    return True




""" 2번: 나의 풀이(구현 방식, 효율성 살짝 떨어짐) """
def solution2(s):
    p, y = 0, 0
    for x in s:
        if x == 'p' or x =='P':
            p += 1
        elif x == 'y' or x =='Y':
            y += 1

    if p == y:
        return True
    else:
        return False




""" 3번: 다른 사람의 풀이 (lower 사용) """
def solution3(s):
    return s.lower().count('p') == s.lower().count('y')

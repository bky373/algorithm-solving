""" 1번: 내가 작성한 풀이 """
def solution(strings, n):
    answer = sorted(strings, key=lambda x: x[n])

    for x in range(len(answer)):
        for y in range(x+1, len(answer)):
            if answer[x][n] == answer[y][n]:
                if answer[x] > answer[y]:
                    answer[x], answer[y] = answer[y], answer[x]

    return answer



""" 2번: 1번 성공 후 참고한 풀이(sorted 한 번 사용) """
def solution2(strings, n):
    return sorted([s for s in strings], key=lambda x: [x[n], x]])



""" 3번: 1번 성공 후 참고한 풀이(sorted 두 번 사용) """
def solution3(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

def solution(n, lost, reserve):
    student = [1] * (n+1)
    ans = 0

    for x in range(1, n+1):
        if x in reserve:
            student[x] += 1
        if x in lost:
            student[x] -= 1

    for x in range(1, n):
        if student[x] > 1 and student[x-1] == 0:
            student[x-1] += 1
            student[x] -= 1

        if student[x] > 1 and student[x+1] == 0:
            student[x+1] += 1
            student[x] -= 1
    if student[-1] == 2 and student[-2] == 0:
        student[-2] += 1
        student[-1] -= 1

    for x in range(1, n+1):
        if student[x] != 0:
            ans += 1
    return ans

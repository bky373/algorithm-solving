"""
<핵심 로직>

남은 날 = (100 - 작업진도) / 작업속도
    if (100 - 작업진도) % 작업속도 != 0
        위의 남은 일수 + 1

현재 완료 개수 +1
현재 작업의 남은 날 >= 다음 작업 남은 날
    현재 작업 남은 날보다 크거나 같은 값이 나올 때까지 이동
        완료 개수 +1 씩 증가
    정답에 완료 개수 더하기 
    남은 작업이 1개일 때 완료 개수 +1 더하기

"""
def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses)

    for x in range(len(progresses)):
        days[x] = (100 - progresses[x]) / speeds[x]
        if  (100 - progresses[x]) % speeds[x] != 0:
            days[x] += 1

    while len(days) >= 2:
        day = days.pop(0)
        completed = 1
        if day >= days[0]:
            while len(days) >= 1 and day >= days[0]: 
                days.pop(0)
                completed += 1
        answer.append(completed)
        if len(days) == 1:
            answer.append(1)

    return answer

answer = solution([93, 30, 55],	[1, 30, 5])
print(answer)

"""
[2, 1]
"""
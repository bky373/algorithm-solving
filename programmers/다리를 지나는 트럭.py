"""
용어 정리>>
    bridge_length: 다리 길이
    bridge_weight: 다리의 최대 하중
    truck_weights: 트럭들의 무게
    passings: 다리 위 트럭의 큐
    times : 트럭들이 다리를 통과한 시간의 큐

핵심 로직>> 큐를 활용한다
    truck_weight이 1 보다 크고, passings의 합과 truck_weights[0]의 합이 bridge_weight보다 작거나 같으면
        times[i]에 +1을 더한다
        truck_weights를 빼서 passings에 더한다 
        만약 passings 길이가 1보다 크면
            times[1]에 +1을 더한다
    truck_weight이 1 이하이거나, passings의 합과 truck_weights[0]이 bridge_weight보다 크면
        times[0] 시간을 +1한다
    times[0]의 시간이 다리 길이와 같으면
        times[0]을 빼서 전체시간에 더한다 
        passings[0]를 빼준다
"""

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_number = len(truck_weights)
    times = [0] * truck_number
    passings = []
    passed = []
    waitings = truck_weights[::-1] 

    while len(passed) != truck_number :
        times[0] += 1
        if times[0] == bridge_length + 1:
            passed.append(passings.pop(0))
            if len(times) > 0 and len(passed) <= 1 :
                answer += times.pop(0)
            else:
                answer += 1
                times.pop(0)
            if len(times) > 0 :
                times[0] += 1
            
        if len(passings) > 1:
                for x in range(1, len(passings)):
                    times[x] += 1
        if len(waitings) >= 1 and (sum(passings) + waitings[len(waitings)-1]) <= weight:
            passings.append(waitings.pop())

        print('passings >>>', passings)
        print('times >>>', times)
        print('>>> answer', answer)
    return answer

# answer = solution(2, 10, [7, 4, 5, 6])
answer = solution(100, 100, [10,10,10,10,10,10,10,10,10])
# answer = solution(100, 100, [10])
print(answer)

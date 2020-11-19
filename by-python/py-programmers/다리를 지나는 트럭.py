def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length
    curr_weight = 0

    while truck_weights:
        answer += 1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out

        if curr_weight + truck_weights[0] > weight:
            bridge_on.append(0)
        else:
            truck = truck_weights.pop(0)
            bridge_on.append(truck)
            curr_weight += truck

    while curr_weight>0:
        answer += 1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out

    return answer

"""
    문제를 풀며...
        이전까지는 큐의 개념을 잘 알고 있다고 생각했다. 
        하지만 활용하려고 하니 아직 한참 멀었다는 것을 깨달았다 ㅠㅠ
        큐를 머릿속에 더 논리적으로 그려볼 수 있는 문제였다.

    Solution
        풀이 출처 https://assaeunji.github.io/python/2020-05-08-pgtruck/

"""

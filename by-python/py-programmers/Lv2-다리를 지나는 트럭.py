def solution(bridge_length, weight, truck_weights):
    seconds = 0
    on_bridge = [0] * bridge_length
    cur_weight = 0

    while truck_weights:
        seconds += 1
        passed = on_bridge.pop(0)
        cur_weight -= passed

        if cur_weight + truck_weights[0] > weight:
            on_bridge.append(0)
        else:
            truck = truck_weights.pop(0)
            on_bridge.append(truck)
            cur_weight += truck

    while cur_weight > 0:
        seconds += 1
        passed = on_bridge.pop(0)
        cur_weight -= passed

    return seconds


if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))

"""
    문제를 풀며...
        이전까지는 큐의 개념을 잘 알고 있다고 생각했다. 
        하지만 활용하려고 하니 아직 한참 멀었다는 것을 깨달았다 ㅠㅠ
        큐를 머릿속에 더 논리적으로 그려볼 수 있는 문제였다.
    
    한 번 더 풀어보면서, 이전보다 훨씬 빠르게 이해되었고,
        큐 활용에 대해 복습할 수 있었다.

    Solution
        풀이 출처 https://assaeunji.github.io/python/2020-05-08-pgtruck/

"""

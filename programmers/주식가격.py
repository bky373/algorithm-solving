from collections import deque

def solution(prices):
    prices_dq = deque(prices)
    answer = [0]*len(prices)

    if len(prices_dq) == 2:
        return [1,0]

    for x in range(len(prices_dq)):
        current_price = prices_dq.popleft()
        
        for next_price in prices_dq:
            answer[x] += 1
            if current_price > next_price:
                break
    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]


"""
<반복문 로직>

prices = ABCD
A를 pop한다
prices = BCD
A와 B,C,D를 비교한다
    A 해당 인덱스의 시간을 1초 올린다
    B가 A보다 높으면 반복문을 빠져나온다
    B가 A보다 낮거나 같으면 C와 D를 차례대로 비교한다

B를 pop한다
prices = CD
B를 C, D와 비교한다
    B 해당 인덱스의 시간을 1초 올린다
    C가 B보다 높으면 반복문을 빠져나온다
    C가 B보다 낮거나 같으면 D를 비교한다

C를 pop한다
prices = D
C를 D와 비교한다
    C 해당 인덱스의 시간을 1초 올린다
    어떤 분기든 반복문을 빠져나온다

*마지막*
D는 내부 반복문을 돌기 전에 빠져나온다

"""
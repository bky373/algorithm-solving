def solution(prices):
    prices_size = len(prices)
    stay_seconds = [0] * prices_size

    for i in range(prices_size):
        for j in range(i + 1, prices_size):
            if prices[i] <= prices[j]:
                stay_seconds[i] += 1
            else:
                stay_seconds[i] += 1
                break

    return stay_seconds


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]

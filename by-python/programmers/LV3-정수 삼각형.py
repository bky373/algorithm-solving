def solution(triangle):
    MAX = 500
    dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]

    answer = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                dp[i][j] = triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            answer = max(answer, dp[i][j])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

def solution(answers):
    n = len(answers)
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]

    for i in range(n):
        if answers[i] == a[i % len(a)]:
            result[0] += 1
        if answers[i] == b[i % len(b)]:
            result[1] += 1
        if answers[i] == c[i % len(c)]:
            result[2] += 1

    max_value = max(result)
    answer = []

    for x in range(3):
        if result[x] == max_value:
            answer.append(x + 1)
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 2, 1, 2, 1, 3, 1, 2, 3]))

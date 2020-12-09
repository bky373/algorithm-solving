def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


if __name__ == '__main__':
    print(solution(input()))

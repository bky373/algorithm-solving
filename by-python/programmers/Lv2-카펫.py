def solution(brown, yellow):
    shape = []
    right_val = brown // 2 - 2
    sqrt_y = int(yellow ** .5)
    for i in range(1, sqrt_y + 1):
        if yellow % i == 0:
            factor1 = i
            factor2 = yellow // i

            if factor1 + factor2 == right_val:
                shape.append(max(factor1, factor2) + 2)
                shape.append(min(factor1, factor2) + 2)
                break
    return shape


if __name__ == '__main__':
    brown = 24
    yellow = 24
    print(solution(brown, yellow))

'''
- 문제: https://programmers.co.kr/learn/courses/30/lessons/42842
- 고려할 사항
    - 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
    - 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
    - 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
- 풀이
    - 위의 문제에서 카펫의 전체 칸 개수는 아래와 같이 나타낼 수 있다.
    - 카펫의 전체 칸 개수 = (노란색 칸 개수 + 갈색 칸 개수) = (노란색 행 개수 + 2(상,하)) * (노란색 열 개수 + 2(좌,우))  
    - 위의 식을 정리하면 아래 식이 나온다. 
        -> 노란색 행 개수 + 노란색 열 개수 = 갈색 칸 개수 / 2 - 2
    - 갈색 칸 개수는 문제에서 주어지므로 노란색 행과 열의 개수만 찾으면 된다. (그리고 이들은 노란색 전체 칸 개수의 약수들이다.)
    - 완전 탐색으로 위의 식을 만족하는 약수들을 찾아가다 발견하면 2씩 더하여 반환한다.    
'''

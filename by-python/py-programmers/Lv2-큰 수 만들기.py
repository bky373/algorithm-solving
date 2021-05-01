# 방법 1
# 반복문과 인덱스를 활용한 풀이 (시도해본 것중 가장 빠른 풀이)
def solution(number, k):
    size = len(number)
    start = 0
    end = start + k
    max_nums = []

    while end < size:
        if not k:
            max_nums.append(''.join(number[start:]))
            break

        max_val = '-1'
        max_idx = 0
        for i in range(start, end + 1):
            num = number[i]
            if num > max_val:
                max_val = num
                max_idx = i

                if max_val == '9':
                    break

        max_nums.append(max_val)

        k -= (max_idx - start)
        start = max_idx + 1
        end = start + k

    return ''.join(max_nums)


# 방법 2
# 스택을 활용한 풀이
def solution_with_stack(number, k):
    size = len(number)
    max_nums = [number[0]]
    idx = 1

    while idx < size:
        if not k:
            max_nums.append(''.join(number[idx:]))
            break

        num = number[idx]
        while max_nums and num > max_nums[-1] and k > 0:
            max_nums.pop()
            k -= 1

        max_nums.append(num)
        idx += 1

    return ''.join(max_nums[:size - k])


if __name__ == '__main__':
    number = "1231234"
    number = "194154993"
    number = "4177252841"
    number = "99999"
    number = "1924"
    k = 2
    print(solution(number, k))
    print(solution_with_stack(number, k))

'''
- 문제: https://programmers.co.kr/learn/courses/30/lessons/42883
- 풀이:
        # 고려할 사항
        1) number는 1자리 이상, 1,000,000자리 이하의 숫자로 문자열로 주어진다
        2) 제거할 수의 개수: k는 1이상 number의 자릿수 미만인 자연수
        3) 남겨야 할 자릿수: number의 길이 - k
        4) number 요소는 0부터 9까지 이다.. (최댓값을 초기화할 때 0으로 하면 최댓값의 인덱스를 찾을 수 없다.)
        
        # 전개 1 - 반복문과 인덱스를 활용한 풀이
        - 특정 범위의 숫자 중 최댓값을 찾고, 매순간 최댓값을 결과에 더해주는 식으로 문제를 풀 수 있다.
        - 특정 범위는 (시작 인덱스부터 k+1번째까지)를 말한다.
        - 시작 인덱스는 반복문을 돌 때마다 (최댓값의 인덱스 + 1)로 업데이트되고, 직전 인덱스와 현재 시작 인덱스의 차이만큼 k가 줄어든다. 
        - k가 0이 되면 굳이 반복문을 돌 필요가 없으므로 나머지 값을 전부 결과에 더한다.

        # 전개 2 - 스택을 활용한 풀이
        - 스택 최상위 숫자가 새로 푸시될 숫자보다 작을 경우, 최상위 숫자를 팝하고 팝할 때마다 k에서 1을 빼준다.
            - 최상위 숫자를 업데이트 해도 새로 푸시될 숫자보다 여전히 작다면, 반복문을 돌려 계속 팝한다.
        - 반대로 최상위 숫자가 크거나 같을 경우, 스택에 푸시한다.
        - 입력값이 한 개의 숫자로만 구성된 경우, 스택에는 모든 숫자가 푸시된다. 
            이를 대비해 마지막에 슬라이싱을 사용하여 필요한 만큼의 길이만 구하여 값을 반환한다.  
        
        # 배운 점
        - 불필요한 반복문은 돌지 말자. 
            - 방법 1에서 특정 범위의 최댓값이 9로 할당되면 이후 반복문을 돌지 않아도 된다!
        - join 함수를 적절히 활용하자. 
            - 방법 1, 2에서 k가 0일 경우, 불필요한 반복문을 돌지 않고 나머지 숫자를 모두 결과에 더해주면 된다.
                이 경우 반복문을 사용하는 것보다 join이 더 빠르게 실행된다는 점 참고하자.
        - 슬라이싱은 되도록 지양하자. 
            - 알고리즘적으로 슬라이싱이 과연 필요할까? 고민해봐야 한다. 
            - 적절한 인덱싱만으로 문제를 해결할 수 있다.
        - 스택 자료구조를 활용하면 생각보다 간단히 문제를 해결할 수 있다.
'''

# 나의 풀이
# 순열을 구현하고 싶었지만 방법이 잘 떠오르지 않아 우선 직관적으로 풀었다.
# 그래서 풀긴 했지만 관련 없는 숫자들까지 체크하다 보니 효율성이 썩 좋지 않다.
# (itertools의 permutations는 배제하고 풀었다.)
def solution(numbers):
    numbers = ''.join(sorted(numbers))
    numbers_set = set(numbers)
    max_val = int(numbers[::-1])
    min_val = max(int(numbers[0]), 2)

    notes = [0] * 10
    for num in numbers:
        notes[int(num)] += 1

    prime_cnt = 0
    for num in range(min_val, max_val + 1):
        str_num = str(num)
        for n in str_num:
            if n not in numbers_set:
                break
        else:
            for factor in range(2, int(num ** .5) + 1):
                if num % factor == 0:
                    break
            else:
                tmp_notes = notes[:]
                for n in str_num:
                    n = int(n)
                    if not tmp_notes[n]:
                        break
                    tmp_notes[n] -= 1
                else:
                    prime_cnt += 1

    return prime_cnt


# 아래 풀이는 두 분의 풀이를 참고하였다.
# Jinsu Lim님의 풀이(https://programmers.co.kr/learn/courses/30/lessons/42839/solution_groups?language=python3)
# Gwon Seonggwang님 풀이(https://programmers.co.kr/learn/courses/30/lessons/42839/solution_groups?language=python3)
# 소수인지 체크할 때(is_prime) 숫자는 제곱근까지만 계산하도록 수정했다.
# 소수 체크 함수(is_prime)는 filter 함수 안에서 사용하였다.
# 위 두 가지 방법을 사용하니 성능이 심하게는 몇백 배 좋아졌다.
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** .5) + 1):
        if number % i == 0:
            return False

    return True


def make_permutations(str1, str2, permutations):
    if str1:
        permutations.add(int(str1))

    for i in range(len(str2)):
        make_permutations(str1 + str2[i], str2[:i] + str2[i + 1:], permutations)


def solution_with_permutations(numbers):
    permutations = set()
    make_permutations("", numbers, permutations)

    return len(list(filter(is_prime, permutations)))


if __name__ == '__main__':
    numbers = "17"
    print(solution(numbers))  # 3
    print(solution_with_permutations(numbers))  # 3

'''
- 문제: https://programmers.co.kr/learn/courses/30/lessons/42839
- 고려할 사항:
    - 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수 개수를 반환한다.
    - 
- 풀이:
'''

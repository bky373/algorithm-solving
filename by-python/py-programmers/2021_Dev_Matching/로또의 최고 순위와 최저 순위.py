# 처음 풀었을 땐 순위 자료구조로 Map을 활용했는데,
# 다른 방법들을 시도해보며 굳이 Map을 활용하지 않아도 된다는 걸 배웠다.

def solution(lottos, win_nums):
    match_result = [6, 6, 5, 4, 3, 2, 1]

    match_count = 0
    for num in lottos:
        if num in win_nums:
            match_count += 1
    zero_count = lottos.count(0)

    best_rank = match_result[match_count + zero_count]
    worst_rank = match_result[match_count]
    return [best_rank, worst_rank]


# 테스트에서는 미세하지만 가장 좋은 성능을 보여줌
def solution2(lottos, win_nums):
    match_count = 0
    zero_count = 0
    for num in lottos:
        if not num:
            zero_count += 1

        elif num in win_nums:
            match_count += 1

    best_match = match_count + zero_count
    worst_match = match_count

    # Lee Yongjun님 풀이 참고
    best_rank = 7 - best_match if best_match >= 1 else 6
    worst_rank = 7 - worst_match if worst_match >= 1 else 6
    return [best_rank, worst_rank]


# set 활용 - Sangwoo Suk님 풀이 참고
# solution 2에 비해 시간이 좀더 걸리는 것 같다.
def solution3(lottos, win_nums):
    zero_count = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)

    worst_match = len(lottos.intersection(win_nums))
    best_match = worst_match + zero_count

    best_rank = 7 - best_match if best_match >= 1 else 6
    worst_rank = 7 - worst_match if worst_match >= 1 else 6
    return [best_rank, worst_rank]


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))
    print(solution2(lottos, win_nums))
    print(solution3(lottos, win_nums))

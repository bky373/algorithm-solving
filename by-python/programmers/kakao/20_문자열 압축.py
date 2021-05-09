def count_num_cnt(duplicates):
    total_num_cnt = 0
    for cnt in duplicates:
        if cnt:
            total_num_cnt += len(str(cnt + 1))
    return total_num_cnt


def solution(s):
    n = len(s)
    c = 0
    min_len = 1000
    while c <= n:
        if min_len <= 2:
            return min_len

        tmp_n = n
        c += 1
        i = 0
        duplicate_cnt = 0
        num_counts = []

        while i < n:
            if s[i:i + c] == s[i + c: i + c * 2]:
                tmp_n -= c
                duplicate_cnt += 1
            else:
                num_counts.append(duplicate_cnt)
                duplicate_cnt = 0
            i += c

        min_len = min(min_len, tmp_n + count_num_cnt(num_counts))
    return min_len


if __name__ == '__main__':
    s = "a" * 1000
    print(solution(s))  # 5

'''
- 어려운 점: 중복되는 개수가 10개 이상일 때 처리하기
    - 단위의 범위는 1부터 문자열의 길이까지이다.
    - 단위별로 문자열을 나누었을 때,
        - 현재 단위 문자열과 다음 단위 문자열이 일치하는 경우
            - 전체 길이에서 단위 길이만큼을 차감한다. 
            - 중복 개수를 1 더해준다.
        - 일치하지 않는 경우
            - 중복 개수를 중복 개수 리스트에 더한다   
            - 중복 개수를 0으로 초기화한다.
        - 현재 위치 인덱스에 단위의 길이만큼을 더한다.
        
    - 중복 개수 리스트를 돌면서
        - 중복 개수가 999 이상이면,
            - 남은 길이에 4를 더한다.
        - 중복 개수가 99 이상이면,
            - 남은 길이에 3을 더한다.
        - 중복 개수가 10 이상이면,
            - 남은 길이에 2를 더한다.
        - 중복 개수가 0 초과 10 미만이면,
            - 남은 길이에 1를 더한다.
    (=> 이 과정은 개수에 1을 더해주고 문자열로 바꾼 뒤, 문자열의 길이를 구해 더해주는 방법으로 수정했다.)
    
    - 남아 있는 길이와 중복 개수 리스트 원소들의 합계를 더하고 현재 최솟값과 비교하여 최솟값을 구한다.          
'''

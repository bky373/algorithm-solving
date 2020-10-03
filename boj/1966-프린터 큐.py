tc = int(input())
answer = []

for c in range(tc):
    count = 0
    n, m = list(map(int, (input().split())))
    priorities = list(enumerate(map(int, (input().split()))))

    while True:
        cur = priorities.pop(0)
        if any(cur[1] < p[1] for p in priorities):
            priorities.append(cur)
        else:
            count += 1
            if cur[0] == m:
                answer.append(count)
                break

for a in answer:
    print(a)

"""
< 핵심 로직 >
    1. 큐에서 첫 번째 원소를 뽑는다
    2. 나머지 원소들 중 우선순위가 더 큰 게 있다면 큐 목록의 뒤로 보낸다
    3. 그렇지 않으면 출력한다
        - count +1 한다
        - 현재 문서가 찾고자 하는 문서의 인덱스와 맞는지 확인한다 (맞다면 break하여 반복문을 빠져나온다)
    4. 1-3번의 과정을 반복한다

"""

N = int(input())
nums = list()

for x in range(int(N)):
    nums.append(int(input()))

popped = [0] * N
prev, next = 0, nums[0]
plus_symbol, minus_symbol = '+', '-'
answer = list()

for i in range(N):
    if prev < next:
        for x in range(prev, next):
            if popped[x] == 0:
                answer.append(plus_symbol)
    elif prev > next:
        for x in range(prev, next, -1):
            if popped[x-1] == 0:
                answer.append(minus_symbol)
                popped[x-1] = 1
   
    popped[next-1] += 1
    answer.append(minus_symbol)
    prev = next    
    if i+1 == N:
        next = N+1
    else: 
        next = nums[i+1]


if any(p == 2 for p in popped):
    print('NO')
else:
    for a in answer:
        print(a)
"""
< 핵심 로직 >
    1. prev = 0, next = 첫번째 원소값 으로 시작
    2. prev < next일 때, prev부터 (next-1)까지 push
        - popped == 0일 경우에만 answer에 '+' append
          (*popped = 0이면 아직 pop되지 않은 상태, 1이면 pop된 상태)
    3. prev > next일 때, prev부터 (next+1)까지 내려오며 pop
        - popped == 0일 경우에만 answer에 '-' append
        - 같은 조건일 때, 해당 인덱스 popped = 1로 수정
    4. popped[next-1] 에 +1 하기 (인덱스는 0부터 시작하므로 next-1을 해줘야 함)
        - 여기서 +1을 해주는 이유는, 이미 pop된 원소가 또다시 pop되는 경우를 계산하기 위함
           (-> 출력 기준이 되므로 중요)
        - answer에 '-' append
    5. prev = next값, next = 다음 인덱스 값 할당
        - 이때 next 다음 인덱스가 없으면 next = 수열의 길이 + 1 (무조건 prev가 작아지게 해 pop되게 하기 위함)
    5. 수열의 길이만큼 2-4번 과정 반복
    6. popped == 2가 하나라도 있으면 No 출력, 그렇지 않으면 answer 차례대로 출력
"""


"""
    다른 문제 풀이 방법 (출처: fastcampus)
"""
n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1): # 데이터 개수만큼 반복
    data = int(input())
    while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        print('NO')
        exit(0)

print('\n'.join(result)) # 가능한 경우

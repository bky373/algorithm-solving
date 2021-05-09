""" 1번: 내가 작성한 코드 """
bucket_list = []
for _ in range(3):
    bucket_list.append(list(map(int, input().split())))

# 0번째: capacity
# 1번째: amount of milk
for x in range(100):
    pour_amount = min(bucket_list[(x+1)%3][0]-bucket_list[(x+1)%3][1], bucket_list[x%3][1])
    bucket_list[x%3][1] -= pour_amount
    bucket_list[(x+1)%3][1] += pour_amount

print('\n'.join([str(bucket[1]) for bucket in bucket_list]))



""" 2번: 1번 성공 후 참고한 코드 """
C, M = [0, 0, 0], [0, 0, 0]

for x in range(3):
    a, b = map(int, input().split())
    C[x] = a
    M[x] = b

for c in range(100):
    x, nx = c % 3, (c + 1) % 3

    M[x], M[nx] = max(M[x]-(C[nx]-M[nx]), 
                        0), min(C[nx], M[x] + M[nx])

for m in M:
    print(m)
    
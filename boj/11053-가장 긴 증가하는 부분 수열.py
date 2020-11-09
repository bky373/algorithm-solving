N = int(input())
A = list(map(int, input().split()))

sub_cnt = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            sub_cnt[i] = max(sub_cnt[i], sub_cnt[j] + 1)
print(max(sub_cnt))

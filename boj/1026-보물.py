N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = sum(map(lambda x: x[0]*x[1], zip(A,B)))
print(S)

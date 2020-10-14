# """ 1번: 내가 작성한 코드 (큐로 접근) """
# import string

# alpha_list = list(string.ascii_uppercase)
# count_list = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
# alpha_count = dict()
# x = 0
# for alpha in alpha_list: 
#     alpha_count[alpha] = count_list[x] 
#     x += 1

# N, M = map(int, input().split())
# A, B = input().split()
# i, j = 0, 0
# C = []

# while i<=len(A) or j <= len(B):
#     if i<len(A):
#         C.append(alpha_count[A[i]])
#     if j<len(B):
#         C.append(alpha_count[B[j]])
#     i += 1
#     j += 1

# while len(C) > 2:
#     c1 = C.pop(0)
#     for x in range(len(C)):
#         c2 = C.pop(0)
#         C.append((c1+c2)%10)
#         c1 = c2

# print("%s%%" % str(C[0]*10+C[1]))



""" 2번: 1번 성공 후 참고한 코드  """
N, M = map(int, input().split())
A, B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len = min(N,M)
for i in range(min_len):
    AB += A[i] + B[i]

AB += A[min_len:] + B[min_len:]

lst = [alp[ord(i)-ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0]%10*10+lst[1]%10))

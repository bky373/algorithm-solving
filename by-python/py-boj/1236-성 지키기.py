""" 1번: 내가 작성한 코드 """
n, m = map(int, input().split())
arrays = []

for _ in range(n):
    arrays.append(input())

empty_row = 0
empty_col = 0

# 행 체크
for array in arrays:
    if all('.' == a for a in array):
        empty_row += 1

# 열 체크
for x in range(m):
    if all('.' == array[x] for array in arrays):
        empty_col += 1

print(max(empty_row, empty_col))




""" 2번: 1번 성공 후 참고한 코드 """
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

col_count = 0
for j in range(m):
    if col[j] == 0:
        col_count += 1

print(max(row_count, col_count))

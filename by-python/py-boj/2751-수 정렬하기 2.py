""" 1. 내가 작성한 코드 (계수 정렬 알고리즘 사용) """
""" 이점: 메모리를 적게 사용함 """
import sys

n = int(sys.stdin.readline())
MAX = 1_000_000
negatives = [0 for _ in range(MAX + 1)]
positives = [0 for _ in range(MAX + 1)]

for _ in range(n):
    number = int(sys.stdin.readline())
    if number >= 0:
        positives[number] += 1
    else:
        negatives[-number] += 1

for x in range(MAX, -1, -1):
    if negatives[x] >= 1:
        print(-x)
for x in range(MAX + 1):
    if positives[x] >= 1:
        print(x)

""" 2. 1번 성공 후 참고한 코드 (병합정렬 이용) """
""" PyPy3으로 제출 """
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

print('\n'.join([ str(n) for n in merge_sort(array)]))

""" 3. 2번과 다른 병합 정렬 코드 """
""" PyPy3 으로 제출 """

def merge_split(data):
    if len(data) <= 1:
        return data
    
    mid = int(len(data) / 2)
    left = merge_split(data[:mid])
    right = merge_split(data[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    l_pointer, r_pointer = 0, 0
    
    while len(left) > l_pointer and len(right) > r_pointer:
        if left[l_pointer] > right[r_pointer]:
            merged.append(right[r_pointer])
            r_pointer += 1
        else:
            merged.append(left[l_pointer])
            l_pointer += 1

    while len(left) > l_pointer:
        merged.append(left[l_pointer])
        l_pointer += 1

    while len(right) > r_pointer:
        merged.append(right[r_pointer])
        r_pointer += 1
    return merged

import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

print('\n'.join([ str(n) for n in merge_split(nums)]))

""" 4. 기본 정렬 함수(sorted) 이용 코드 """
""" PyPy3 으로 제출 """
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array)

for data in array:
    print(data)
    
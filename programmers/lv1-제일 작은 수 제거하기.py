def solution(arr):
    min_x = min(arr)
    return [n for n in arr if n != min_x] if arr else [-1]

# """
#     1. 내가 작성한 코드 (시간초과로 실패) 
# """
# tc = int(input())
# for _ in range(tc):
#     data = input()
#     l = len(data)

#     stack= list(data[::-1])
#     password = [0] * l
#     cursor = 0

#     while stack:
#         letter = stack.pop()
#         if letter == '-':
#             if len(password) > 0:
#                 password.pop(cursor-1)
#         elif letter == '<':
#             if cursor > 0:
#                 cursor -= 1
#         elif letter == '>':
#             if cursor <= l:
#                 cursor += 1
#         else:
#             if password[cursor] != 0:
#                 password = password[:cursor] + [letter] + password[cursor:]  
#             else:
#                 password[cursor] = letter
#             cursor += 1

#     print(''.join([p for p in password if p != 0]))

"""
< 핵심 로직 >
    - 최대 L의 길이가 1,000,000개 이므로, 문제에서 요구하는 대로만 구현하면(시뮬레이션 방식을 사용하면) 문제를 해결할 수 없다
    - 다시 말해, 적절한 알고리즘을 설계해서 문제를 풀어야 한다
    - 여기에서는 스택을 활용하여 선형시간(O(n)) 문제를 해결할 수 있는 알고리즘을 설계한다.

    1. 스택 두 개를 만들고, 스택 두 개의 중간 지점을 cursor로 간주한다
    2. 문자 입력: 왼족 스택에 원소를 삽입한다
    3. '-' 입력: 왼쪽 스택에서 원소를 제거한다
    4. '<' 입력: 왼쪽 스택에서 오른쪽 스택으로 원소를 이동한다
    5. '>' 입력: 오른쪽 스택에서 왼쪽 스택으로 원소를 이동한다

    출처 : fastcampus
    
"""

test_case = int(input())

for _ in range(test_case):
    left_stack, right_stack = [], []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
    
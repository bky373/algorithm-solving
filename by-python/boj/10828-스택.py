from collections import deque

import sys

input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return int(len(self.data) == 0)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            return -1

        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return -1

        return self.data[-1]


st = Stack()
N = int(input())

for _ in range(N):
    lines = input().split()

    cmd = lines[0]
    if cmd == 'push':
        st.push(lines[1])

    elif cmd == 'pop':
        print(st.pop())

    elif cmd == 'top':
        print(st.peek())

    elif cmd == 'empty':
        print(st.is_empty())

    elif cmd == 'size':
        print(len(st))

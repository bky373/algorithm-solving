# 시간 복잡도: O(N)
# 접근: 큐를 활용, 최대 우선순위가 무엇인지 알기 위해 배열을 하나 더 만듦
# 참고: 최대 우선순위가 바뀔 때 최대 10번 반복문을 돌아야 해서
#      O(10*N)의 시간 복잡도가 나오지만, 시간 복잡도 계산시 앞의 계수는 없애므로 O(N)의 시간이 걸림

from collections import deque


def solution(priorities, location):
    priority_counts = [0] * 10
    max_priority = -1
    for priority in priorities:
        priority_counts[priority] += 1
        max_priority = max(priority, max_priority)

    queue = deque(enumerate(priorities))
    print_order = 0
    while queue:
        now = queue.popleft()
        now_priority = now[1]

        if now_priority < max_priority:
            queue.append(now)
        else:
            print_order += 1
            priority_counts[now_priority] -= 1

            if now[0] == location:
                break

            if not priority_counts[now_priority]:
                for i in range(now_priority - 1, 0, -1):
                    if priority_counts[i]:
                        max_priority = i
                        break
    return print_order


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))

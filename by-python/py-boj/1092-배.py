import sys

input = sys.stdin.readline


def solve(capacities, boxes):
    carry_position = [0] * len(capacities)
    checked = [False] * len(boxes)
    result = 0
    cnt = 0

    if boxes[0] > capacities[0]:
        return -1

    while True:
        if cnt == len(boxes):
            break
        for i in range(len(capacities)):
            while carry_position[i] < len(boxes):
                if not checked[carry_position[i]] and capacities[i] >= boxes[carry_position[i]]:
                    checked[carry_position[i]] = True
                    carry_position[i] += 1
                    cnt += 1
                    break
                carry_position[i] += 1
        result += 1
    return result


if __name__ == '__main__':
    n = int(input())
    capacities = list(map(int, input().split()))
    m = int(input())
    boxes = list(map(int, input().split()))

    capacities.sort(reverse=True)
    boxes.sort(reverse=True)

    print(solve(capacities, boxes))

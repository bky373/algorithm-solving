from collections import deque


def bfs(begin, target, words):
    size = len(begin)
    queue = deque([(begin, 0)])

    while queue:
        word, step = queue.popleft()

        if word == target:
            return step

        for compare_word, compare_step in words:
            diff = 0

            for i in range(size):
                if diff > 1:
                    break

                if word[i] != compare_word[i]:
                    diff += 1

            if diff == 1:
                words.remove((compare_word, compare_step))
                queue.append((compare_word, step + 1))

    return 0


def solution(begin, target, words):
    words = list(zip(words, [0] * len(words)))
    return bfs(begin, target, words)


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))

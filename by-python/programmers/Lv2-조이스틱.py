def count_min_updown(alphabet, a_order, z_order):
    return min(ord(alphabet) - a_order, z_order - ord(alphabet) + 1)


def count_min_step(name):
    a_order, z_order = (ord('A'), ord('Z'))
    prev = 0
    step = 0

    for i in range(len(name)):
        alpha = name[i]

        if alpha == 'A':
            continue

        step += count_min_updown(alpha, a_order, z_order)
        step += i - prev
        prev = i

    return step


def solution(name):
    a_order, z_order = (ord('A'), ord('Z'))
    size = len(name)

    step = count_min_step(name)

    if not step:
        return step

    # 'A' 아닌 문자 위치 찾기
    stop_idx = 0
    for i in range(size):
        if name[i] != 'A':
            stop_idx = i
            break

    # 'A' 아닌 문자 이후부터 reverse
    reverse_name = name[:stop_idx:-1]
    stop_updown = count_min_updown(name[stop_idx], a_order, z_order)

    if not reverse_name:
        stop_idx = 0

    stop_step = stop_updown + stop_idx * 2 + 1
    reverse_step = stop_step + count_min_step(reverse_name)
    return min(step, reverse_step)


if __name__ == '__main__':
    # result = solution("JEROEN")  # 56
    # result = solution("ABAAAAAABAAABAAAA")  # 14
    # result = solution("ABBAAAAAB")  # 11
    # result = solution("AAABAAAAAB")  # 9
    result = solution("AAAB")  # 2

    print(result)

'''
# 프로그래머스 - Lv2 조이스틱

## 1. 문제

> https://programmers.co.kr/learn/courses/30/lessons/42860

## 2. 고려할 점

- 조이스틱으로 알파벳 이름을 완성하는 문제다.

- 맨 처음엔 A로만 이루어져 있다.

  - ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

- 조이스틱을 각 방향으로 움직이면 아래와 같다.

  ```
  ▲ - 다음 알파벳
  ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
  ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
  ▶ - 커서를 오른쪽으로 이동
  ```

##### 입출력 예

| name     | return |
| -------- | ------ |
| "JEROEN" | 56     |
| "JAN"    | 23     |

- name은 알파벳 대문자로만 이루어져 있다.
- name의 길이는 1 이상 20 이하이다.
- 1) 위치 시작점은 왼쪽 또는 오른쪽이 될 수 있다.
  2) 알파벳 순서 시작점은 A 또는 Z가 될 수 있다. 
     (사실 Z를 시작점으로 한다고 해도 무조건 A에서 시작해야 하므로 이 경우 개수에 1을 더해준다)

## 3. 풀이

- 아래 두 가지 경우의 횟수를 비교한 후 최솟값을 구한다.
  - 1번 - 왼쪽에서 시작하여 마지막까지 방향을 바꾸지 않을 때의 횟수
  - 2번 - 왼쪽에서 시작해 가다 방향을 틀어 첫번째 위치로 이동한 후, 마지막 문자에서부터 왼쪽 방향으로 계산했을 때의 횟수  
  - 2번의 경우, 방향을 트는 시점은 A가 아닌 문자가 나올 때이다.
- 왜 방향 트는 걸 한 번만 허용해야 할까?
  - 문제 조건을 보면, 마지막 문자에서 오른쪽 방향으로 이동했을 때 첫 번째 위치로 이동한다는 말이 없기 때문이다.
    즉, 마지막 문자에서 첫 번째 문자로 바로 이동할 수 없다. (단, 첫 번째 위치에서 마지막 문자로 곧장 이동할 수는 있다.)

## 4. 풀이 코드
- 위의 코드 참고

## 5. 주의할 점

- 주의할 점
  - 질문목록을 보면 알겠지만, 본 문제는 여러 사람들에 의해 테스트 케이스 오류가 많이 제기되는 문제다. 
    여러가지가 건의되고 있으니, 추후에 다시 한 번 살펴보면 좋을 것 같다.  

## 6. 배운 점

- 배운 점
  - 함수를 작성할 때 반복되는 로직을 줄이고 재사용성을 높일 수 있다.
  - 불필요한 반복문을 돌지 않는 로직을 생각해볼 수 있다. 
'''

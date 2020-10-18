
""" 1번: 내가 작성한 코드(정렬 이용) """
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for x, name in enumerate(participant):
        if x == len(completion):
            return name
        if name != completion[x]:
            return name


""" 2번: 1번 성공 후 참고한 코드(해시함수 이용) """
def solution2(participant, completion):
    tmp = 0
    player = dict()
    for p in participant:
        player[hash(p)] = p
        tmp += int(hash(p))
    for c in completion:
        tmp -= int(hash(c))
    return player[tmp]

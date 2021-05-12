def solution(record):
    result = []
    users_dict = dict()
    messages = [u"{name}님이 들어왔습니다.", u"{name}님이 나갔습니다."]

    for line in record:
        cmd = line.split()
        if cmd[0] == 'Enter':
            users_dict[cmd[1]] = cmd[2]
            result.append((cmd[1], 0))

        elif cmd[0] == 'Leave':
            result.append((cmd[1], 1))

        elif cmd[0] == 'Change':
            users_dict[cmd[1]] = cmd[2]

    for i in range(len(result)):
        uid, message_idx = result[i]
        result[i] = messages[message_idx].format(name=users_dict[uid])

    return result


if __name__ == '__main__':
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]

    print(solution(record))

"""
- 문제: https://programmers.co.kr/learn/courses/30/lessons/42888
- 풀이: 구현, 딕셔너리 사용
    - uid를 키로, 닉네임을 값으로 하는 유저 딕셔너리를 만든다. 
    - Enter 명령일 때 결과 배열에 uid와 "님이 들어왔습니다." 메시지 인덱스를 저장한다.
    - Leave 명령일 때 결과 배열에 uid와 "님이 나갔습니다." 메시지 인덱스를 저장한다.  
    - Change 명령일 때 uid 키의 값을 변경한다.
    - 마지막으로 결과 배열을 차례대로 돌면서 uid와 메시지를 변환하여 다시 저장 후 반환한다.
"""

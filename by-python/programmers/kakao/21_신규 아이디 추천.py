# 나의 풀이
# 정규식 표현을 사용하면 이보다 간결하게 작성가능하다.
# 단, 정규식을 사용했을 때 이 문제의 경우
# 성능이 최대 10배까지 떨어져 효율성이 아쉽다.
def remove_first_and_last_dot(text):
    if text and text[0] == '.':
        text = text[1:]

    if text and text[-1] == '.':
        text = text[:-1]

    return text


def solution(new_id):
    punctuations = '~!@#$%^&*()=+[{]}:?,<>/'
    max_length = 15
    tmp_id = []

    for i in range(len(new_id)):
        character = new_id[i]

        # 1단계 - 대문자를 소문자로 치환
        if 'A' <= character <= 'Z':
            character = chr(ord(character) + 32)

        # 2단계 - 특수 문자 제거
        if character in punctuations:
            continue

        tmp_id.append(character)

    # 3단계 - 2번 이상 연속된 마침표(.)을 하나의 마침표(.)로 치환
    next_tmp_id = []
    size = len(tmp_id)
    for i in range(size):
        if i < size - 1 and tmp_id[i] == '.' and tmp_id[i + 1] == '.':
            continue

        next_tmp_id.append(tmp_id[i])

    # 4단계 - 맨 앞의 마침표(.)와 맨 뒤의 마침표(.) 제거
    tmp_id = remove_first_and_last_dot(next_tmp_id)

    # 5단계 - 빈 문자열이라면, "a"를 대입
    if not len(tmp_id):
        tmp_id = ['a']

    # 6단계 - 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #       - 제거 후 마침표(.)가 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    tmp_id = tmp_id[:max_length]
    tmp_id = remove_first_and_last_dot(tmp_id)

    # 7단계 - 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    for i in range(3 - len(tmp_id)):
        tmp_id.append(tmp_id[-1])

    new_id = ''.join(tmp_id)
    return new_id


# Backkom님 풀이 참고
# https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3
import re


def solution_with_regex(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = 'a' if len(new_id) == 0 else new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = new_id if len(new_id) > 2 else new_id + ''.join(new_id[-1] for _ in range(3 - len(new_id)))
    return new_id


if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    print(solution(new_id))
    print(solution_with_regex(new_id))

'''
- 문제: https://programmers.co.kr/learn/courses/30/lessons/72410
- 시간 복잡도:
- 풀이:
        # 고려 사항
        - 아이디의 길이는 3자 이상 15자 이하
        - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용가능
        - 마침표(.)는 처음과 끝에 사용할 수 없고 연속으로 사용할 수 없다
        - 카카오 아이디 규칙:
            신규 유저가 입력한 아이디가 new_id 라고 한다면,
            - 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
            - 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
            - 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
            - 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
            - 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
            - 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
                 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
            - 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
        - new_id는 길이 1 이상 1,000 이하인 문자열
        - new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성
        - new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정
'''

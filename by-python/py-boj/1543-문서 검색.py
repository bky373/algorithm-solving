""" 1번: 내가 작성한 코드 """
line = input()
token = input()
print(len(line.split(token))-1)

""" 2번: 1번 성공 후 참고한 코드 """
document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)

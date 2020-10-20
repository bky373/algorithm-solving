""" 1번: 내가 작성한 풀이 """
def solution(phone_book):
    lengths = set()
    pb_dict = dict()

    for p in phone_book:
        lengths.add(len(p))

    phone_book.sort()

    for l in lengths:
        for p in phone_book:
            if l > len(p):
                continue
            if p[:l] in pb_dict.keys() and p[:l] in pb_dict.values():
                return False 
            pb_dict[p[:l]] = p
    return True


""" 2번: 1번 성공 후 참고한 풀이 """
def solution2(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for x in range(len(phone_book)):
        for j in range(x+1, len(phone_book)):
            if phone_book[j][:len(phone_book[x])] == phone_book[x]:
                return False
    return True

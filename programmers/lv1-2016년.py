""" 1번: 나의 풀이 """
def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    theday = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    past_days = 0
    for x in range(a-1):
        past_days += days[x]
    past_days += b-1
    
    return theday[past_days%7]




""" 2번: 다른 사람의 풀이 """
def solution2(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return days[(sum(months[:a-1])+b-1)%7]

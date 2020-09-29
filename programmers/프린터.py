def findMax(waiting_docs):
    max_priority = 0
    for i in range(len(waiting_docs)):
        if waiting_docs[i][1] > max_priority:
            max_priority = waiting_docs[i][1]
    return max_priority

def solution(priorities, location):
    printed_docs = []
    indices = [i for i in range(len(priorities))]
    waiting_docs = list(zip(indices, priorities))
    hasMax = False

    while waiting_docs:
        
        max_priority = findMax(waiting_docs)
        curr_priority = waiting_docs.pop(0)
        
        for x in range(len(waiting_docs)):
            if waiting_docs[x][1] == max_priority:
                hasMax = True
                break
            else:
                hasMax = False
        
        if curr_priority[1] < max_priority:
            if hasMax:
                waiting_docs.append(curr_priority)
        else:
            printed_docs.append(curr_priority)

    for x in range(len(printed_docs)):
        if printed_docs[x][0] == location:
            return x+1

print(solution([2, 1, 3, 2, 2, 3], 5)) # 2

import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

tc = int(input())
for _ in range(tc):
    operators_list = []
    n = int(input())
    recursive([], n-1)
    
    nums = [ x for x in range(1, n+1) ]

    for operators in operators_list:
        exp = ""
        for x in range(n-1):
            exp += str(nums[x]) + operators[x]
        exp += str(nums[-1])
        if eval(exp.replace(" ","")) == 0:
            print(exp)
    print()

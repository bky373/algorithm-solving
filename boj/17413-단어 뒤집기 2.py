S = input()
tmp, result = "", ""
has_arrow = False

for letter in S:
    if letter == ' ':
        if not has_arrow:
            result += tmp[::-1] + ' '
            tmp = ""
        else: result += ' '
    elif letter == '<':
        has_arrow = True
        result += tmp[::-1] + '<'
        tmp = ""
    elif letter == '>':
        has_arrow = False
        result += '>'
    else:
        if has_arrow: result += letter
        else: tmp += letter

result += tmp[::-1]
print(result)

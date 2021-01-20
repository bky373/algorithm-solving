if __name__ == '__main__':
    while True:
        text = input()
        if text == '.': break

        st = []
        res = 'yes'
        for t in text:
            if t == '.':
                break
            elif t in ['(', '[']:
                st.append(t)
            elif t in [')', ']']:
                if len(st) == 0:
                    res = 'no'
                else:
                    top = st.pop()
                    if (top == '[' and t == ')') or \
                            (top == '(' and t == ']'):
                        res = 'no'
            if res == 'no': break
        print(res if len(st) == 0 else 'no')

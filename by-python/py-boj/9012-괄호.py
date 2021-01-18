def main():
    tc = int(input())
    for _ in range(tc):
        st = []
        braces = input()
        stop = False
        for b in braces:
            if b == '(':
                st.append(b)
            else:  # b == ')'일 때
                if st:  # st에 '("가 하나라도 있으면
                    st.pop()
                else:  # 없으면 )가 무의미하게 더 많으므로 NO 출력
                    print('NO')
                    stop = True
                    break

        if not stop:
            if st:
                print('NO')
            else:
                print('YES')


if __name__ == '__main__':
    main()

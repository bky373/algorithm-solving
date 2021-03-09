while True:
    n = int(input())
    if not n: break

    strings = []
    for _ in range(n):
        strings.append(input())

    sorted_strings = [sorted(s) for s in strings]
    matches = [0] * len(strings)
    mx_anagrams_count = 0
    for i in range(len(strings)):
        for j in range(len(strings)):
            if sorted_strings[i] == sorted_strings[j]:
                matches[i] += 1
            mx_anagrams_count = max(mx_anagrams_count, matches[i])

    mx_anagrams_index = matches.index(mx_anagrams_count)
    print(strings[mx_anagrams_index], mx_anagrams_count - 1)

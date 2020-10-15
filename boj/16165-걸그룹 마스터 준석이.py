n, m = map(int, input().split())
teams = dict()

for _ in range(n):
    team_name, mem_num = input(), int(input())
    teams[team_name] = [input() for _ in range(mem_num)]

for _ in range(m):
    name = input()
    if int(input()):
        for team_name, members in teams.items():
            if name in members:
                print(team_name)
    else:
        print('\n'.join(sorted(teams[name])))

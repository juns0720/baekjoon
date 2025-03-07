import sys
input = sys.stdin.readline



for tc in range(int(input())):
    n = int(input())
    st = list(map(int,input().split()))
    team_score = [[] for _ in range(201)]
    team_cnt = [0 for _ in range(201)]
    check = []
 
    can = {}
    for i in range(1,n+1):
        team_cnt[st[i-1]] += 1
        if team_cnt[st[i-1]] > 5:
            can[st[i-1]] = 1
    crnt_score = 1        
    for i in range(1,n+1):
        if st[i-1] in can:
            team_score[st[i-1]].append(crnt_score)
            crnt_score+=1
    
    for team_number in range(1,201):
        if len(team_score[team_number]) < 6:
            continue
        score = sum(team_score[team_number][0:4])
        check.append((score,team_score[team_number][4],team_number))
    check.sort(key = lambda x: (x[0],x[1]))
    print(check[0][2])
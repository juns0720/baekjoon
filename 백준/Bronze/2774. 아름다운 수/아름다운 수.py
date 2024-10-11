import sys
input = sys.stdin.readline



for tc in range(int(input())):
    cnt = 0
    visited = [0 for i in range(11)]
    num = list(input().strip())
    for n in num:
        n = int(n)
        if not visited[n]:
            visited[n] = 1
            cnt+=1
    print(cnt)


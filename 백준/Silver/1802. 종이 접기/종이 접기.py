import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    paper = input().strip()
    can = True
    while can and len(paper) != 1:
        for i in range(len(paper)//2):
            if paper[i] == paper[-(i+1)]:
                print("NO")
                can = False
                break
        if can == True:
            paper = paper[0:len(paper)//2]

    if can == True:
        print('YES')
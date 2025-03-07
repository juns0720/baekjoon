import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    note1 = set(list(map(int,input().split())))

    m = int(input())
    for i in list(map(int,input().split())):
        if i in note1:
            print(1)
        else:
            print(0)
import sys
input = sys.stdin.readline
S = set()

for _ in range(int(input())):
    cmd = input().split()

    if len(cmd) == 2:
        x = int(cmd[1])
        if cmd[0] == "add":
            S.add(x)
        elif cmd[0] == "remove":
            if x in S:
                S.remove(x)
        elif cmd[0] == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd[0] == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)
    else:
        if cmd[0] == "all":
            S = {i for i in range(1,21)}
        elif cmd[0] == "empty":
            S = set()


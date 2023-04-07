import sys
input = sys.stdin.readline

ml = list(map(int,input().split()))

res1 = 0
res2 = 9
for i in ml:
    if ml[0] == 1:
        if res1+1 == i:
            res1+=1
    elif ml[0] == 8:
        if res2-1 ==i:
            res2-=1
if res1 == 8:
    print("ascending")
elif res2 == 1:
    print("descending")
else:
    print("mixed")

    
import sys
input = sys.stdin.readline

l1 = list(map(int,input().split()))
flag = True
for i in range(1,len(l1)):
    if l1[i] < l1[i-1]:
        flag = False
        break
print("Good" if flag == True else "Bad")
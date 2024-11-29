import sys
input = sys.stdin.readline

'''
1. 양수 양수 : 묶는다 i 2번 증가
2. 양수 음수 : 스킵 i 1번 증가
3. 음수 음수 : 묶는다
3. 양수 0 : 스킵 i 1번 증가
4. 음수 0 : 묶는다 i 2번 증가
'''
n = int(input())

lst = sorted([int(input()) for _ in range(n)], reverse=True)


res = 0
i = 0
tmp = []
while i < n:
    if lst[i] > 0:
        tmp.append(lst[i])
        if len(tmp) == 2:
            if tmp[0] == 1 or tmp[1] == 1:
                res += sum(tmp)
            else:
                res += tmp[0]*tmp[1]
            tmp = []
        i+=1
    else:
        break

if tmp:
    res += sum(tmp)
tmp = []
n-=1
while n > i-1:
    tmp.append(lst[n])
    if len(tmp) == 2:
        res += tmp[0]*tmp[1]
        tmp = []
    n-=1
if tmp:
    res += sum(tmp)    

print(res)
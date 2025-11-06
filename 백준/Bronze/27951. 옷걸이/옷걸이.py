import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
u, d = map(int, input().split())

cnt1 = lst.count(1)
cnt2 = lst.count(2)
cnt3 = n - cnt1 - cnt2

# 가능성 판정
if cnt1 > u or cnt2 > d:
    print("NO")
    exit()

nu = u - cnt1 
nd = d - cnt2  

res = []
for i in lst:
    if i == 1:
        res.append('U')
    elif i == 2:
        res.append('D')
    else:  
        if nu > 0:
            res.append('U')
            nu -= 1
        else:
            res.append('D')
            nd -= 1

print("YES")
print(''.join(res))
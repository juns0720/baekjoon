n,m = map(int,input().split())
str = []
for i in range(m):
    str.append(list(input().strip().split()))
str.sort(key = lambda x:(int(x[1]),int(x[0])))
for i in range(m):
    print(str[i][2],end='')
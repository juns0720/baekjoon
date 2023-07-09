N,M = map(int,input().split())

stack = [i for i in range(1,N+1)]
temp = ''
def cal(N,M,temp):
    if len(temp) == M:
        print(temp.replace('',' ').lstrip())
        return
    for i in range(1,N+1):
        if str(i) not in temp:
            cal(N,M,temp+str(i))

cal(N,M,temp)

        

import sys
input = sys.stdin.readline

def pm_pop():
    plus.pop()
    minus.pop()
def pm_append(cnt,i):
    plus.append(cnt+int(i))
    minus.append(cnt-int(i))
def cal(cnt):
    if 'x' not in num:
        num[-1]+=1
        pm_pop()
        return
    else:
        for i in range(1,N+1):
            if num[i-1] =='x':
                if cnt+int(i) not in plus and cnt-int(i) not in minus:    
                    pm_append(cnt,i)
                    num[i-1] = 'o'
                    cal(cnt+1)
                    num[i-1] = 'x'
        if cnt > 2:
           pm_pop()

N = int(input())
num = ['x' for _ in range(N)]
num.append(0)
for i in range(1,N+1):
    plus = [1+i]
    minus = [1-i]
    num[i-1] = 'o'
    cal(2)
    num[i-1] = 'x'
print(num[-1])
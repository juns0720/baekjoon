import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

res = int(input())

def recursion(i, cnt):
    num = list(map(int,str(int(i))))
    if len(num) == 11:
        return

    if num == sorted(set(num), reverse = True):
        if cnt == res:
            print(i)
            exit()
        recursion(i+1,cnt+1)
        return
    else:
        for j in range(1,len(num)):
            if num[j] >= num[j-1]:
                num[j-1]+=1
                next_num = int(''.join(map(str, num[:j])))*(10**(len(num)-j))
                recursion(next_num, cnt)
                return


recursion(0, 0)
print(-1)
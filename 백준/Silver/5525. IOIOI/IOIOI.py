import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
s = list(input().strip())
end = 2*N+1
cnt = 0
def check(str,cnt):
    temp = 'O'
    for i in str:
        if i != temp:
            temp = i
        else:
            cnt-=1
            break
    return cnt
for i in range(len(s)):
    if s[i] == 'I':
        tmp = s[i:i+end]
        if len(tmp) == end:
            cnt+=check(tmp,1)
print(cnt)  
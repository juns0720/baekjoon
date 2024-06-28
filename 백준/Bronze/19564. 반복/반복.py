import sys
input = sys.stdin.readline


    
s = input().strip()

tmp = list('abcdefghijklmnopqrstuvwxyz')
max_len = len(s)
cnt =  0
i = 0
while i < len(s):
    
    for j in tmp:
        if i >= len(s):
            break
        if j == s[i]:
            i+=1
    cnt+=1
print(cnt)
import sys
input = sys.stdin.readline


while True:
    s = list(input().strip())
    if s[0] == '0':
        break
    ans = "yes"
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            ans = "no"
            break
            
    print(ans)
    
s = list(input().strip())
sum = 0
for i in range(len(s)):
    if s[i] == '0':
        sum-=int(s[i-1])
        sum+=int(s[i-1])*10
    else:
        sum+=int(s[i])
print(sum)
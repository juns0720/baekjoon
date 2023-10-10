s = [0,0]
for i in range(int(input())):
    if abs(s[0] -s[1]) >1:
        break
    if input() == 'D':
        s[0]+=1
    else:
        s[1]+=1
print(s[0],':',s[1],sep='')
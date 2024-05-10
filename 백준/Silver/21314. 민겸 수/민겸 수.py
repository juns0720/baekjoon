import sys
input = sys.stdin.readline


s1 = list(input().strip())

result = ['','']
cnt = 0
start=0
for i in range(len(s1)):
    if s1[i] =='M':
        cnt+=1
        if len(s1)-1 == i:
            if len(s1)-start == cnt:
                result[0] += '1'*cnt
            else:
                result[0]+=str(10**(cnt-1))
            result[1]+=str(10**(cnt-1))
            
    elif s1[i] == 'K':
        if cnt == 0:
            result[0]+='5'
            result[1]+='5'

        else:
            result[0]+=str(5*10**(cnt))
            result[1]+=((str(10**(cnt-1)))+'5')
        cnt = 0
        start=i+1
    
for i in result:
    print(i)


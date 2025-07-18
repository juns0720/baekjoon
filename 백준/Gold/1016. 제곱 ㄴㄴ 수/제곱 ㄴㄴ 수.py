import sys
input = sys.stdin.readline

def find():
    cnt = 0
    for i in range(2,e+1):
        if i == 1:
            continue
        j = (mi // i**2)*i**2
        if j < mi:
            j += i**2
        while j < ma+1:
            if j < mi or j > ma:
                continue
            if j not in dic:
                cnt += 1
            dic[j] = 0
            j += i**2
        
    return cnt

mi,ma = map(int,input().split())

s, e = int(mi**0.5), int(ma**0.5)
dic = dict()
print(ma-mi+1-find())
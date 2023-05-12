import sys
input = sys.stdin.readline

s,k,h = map(int,input().split())
sd = dict()
sd[s] = "Soongsil"
sd[k] = "Korea"
sd[h] = "Hanyang"
if s+k+h < 100:
    print(sd[min(s,h,k)])
else:
    print("OK")
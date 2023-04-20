import sys
input = sys.stdin.readline

sec = []
Sec = 0
for i in range(4):
    Sec+=int(input())
if Sec >=60:
    Min = Sec//60
    Sec%=60
print(Min),print(Sec)

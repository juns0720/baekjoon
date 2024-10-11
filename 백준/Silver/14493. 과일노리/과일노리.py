import sys
input = sys.stdin.readline

n = int(input())

time = 0


for i in range(n):
    a,b = map(int,input().split())
    bot = 0
    while bot <= time:
        bot+=b
        if bot >= time:
            time+=(bot-time)
            break
        if bot <= time < bot + a:
            break
        bot+=a

    time+=1
print(time)
import sys
input = sys.stdin.readline
N = int(input())

time = list(map(int,input().split()))
fees = [0 for i in range(2)]    # 0 - Y, 1 - M

for i in range(len(fees)):
    if i == 0:
        for cost in time:
            if cost % 30 == 0:
                fees[0] += (cost//30 + 1) * 10
            else:
                fees[0] += (cost//30) * 10 + 10
    elif i == 1:
        for cost in time:
            if cost % 60 == 0:
                fees[1] += (cost//60 + 1) * 15
            else:
                fees[1] += (cost//60) * 15 + 15
if fees[0] < fees[1]:
    print('Y',fees[0])
elif fees[0] > fees[1]:
    print('M',fees[1])
else:
    print('Y M',fees[0])
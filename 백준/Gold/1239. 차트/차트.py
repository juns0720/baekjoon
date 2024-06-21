import sys
from itertools import permutations 
input = sys.stdin.readline

n = int(input())

total_data = list(map(int,input().split()))
max_res = 0

if max(total_data) > 50:
    print(0)
else:
    for i in list(permutations(total_data)):
        res = 0
        data = list(i)
        sum_data = 0
        data2 = []
        for i in range(len(data)):
            sum_data+=data[i]
            data2.append(sum_data)
        for i in range(0, len(data2)-1):
            for j in range(i+1, len(data2)):
                if data2[i] + 50 == data2[j]:
                    res+=1
        max_res = max(max_res, res)
    print(max_res)


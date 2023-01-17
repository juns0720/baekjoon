import sys
input = sys.stdin.readline

s_list = list(input().split())
count = 0
for i in range(len(s_list)):
    count+=1
print(count)
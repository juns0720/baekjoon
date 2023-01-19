import sys
input = sys.stdin.readline

num = int(input())
n_list = []
for i in range(num):
   n_list.append(int(input()))
n_list.sort()

for i in range(num):
    print(n_list[i])
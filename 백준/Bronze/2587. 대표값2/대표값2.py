import sys

input = sys.stdin.readline

n_list = []
avg = 0
for i in range(5):
 n_list.append(int(input()))

n_list.sort()       #요소 정렬 
avg = sum(n_list)//5      #리스트 요소 더하기


print(avg,n_list[2])
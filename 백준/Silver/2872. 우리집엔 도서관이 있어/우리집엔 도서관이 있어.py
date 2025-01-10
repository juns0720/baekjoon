import sys
input = sys.stdin.readline

'''
1. 기본적으로 큰 숫자부터 꺼내면 정렬이 가능하다. -> 최대 N회로 무조건 정렬 가능
2. 가장 큰 숫자의 위치부터 내려가면서 순차적으로 정렬되어 있는 숫자의 개수를 검사
'''

N = int(input())
sequence = []
for i in range(N):
    num = int(input())
    if num == N:
        idx = i
    sequence.append(num)

res = 1
prev = N-1

for i in range(idx,-1,-1):
    if sequence[i] == prev:
        res+=1
        prev-=1
print(N-res)
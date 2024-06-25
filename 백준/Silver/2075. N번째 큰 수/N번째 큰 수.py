
"""
heapq를 통해 N번째 큰수를 출력한다.
메모리 제한은 12 x 10^6 Byte이다.
Int형 하나의 크기는 4Byte
즉 배열에 Int형 변수가 3 x 10^6 Byte만큼 입력이 가능하다.

N이 가질 수 있는 최대 수는 1500이다.
따라서 1500 X 1500 =  4 x 2.25 x 10^6승 만큼의 배열 입력이 필요하다.
따라서 최대 입력인 1500 x 1500은 메모리 초과가 발생한다.

1. heap을 생성한 후 N개만큼 힙을 채운다.
2. heap에서 최솟값을 꺼내 다음값와 비교한다.
 2.1 최솟값이 다음값보다 더 큰 경우 최솟값을 다시 heap에 넣는다
 2.2 다음값이 더 큰 경우 heap에 다음값을 넣는다
3. 모든 원소에 대해 검사한 후 heap에서 최솟값을 뽑는다.(해당 값이 N번째 큰 수)
"""


import sys
import heapq

N = int(input())
input = sys.stdin.readline
heap = []

for _ in range(N):
    for cur_num in list(map(int,input().split())):
        if len(heap) < N:
            heapq.heappush(heap,cur_num)
        else:
            min_num = heapq.heappop(heap)
            if min_num < cur_num:
                heapq.heappush(heap,cur_num)
            else:
                heapq.heappush(heap, min_num)
print(heapq.heappop(heap))

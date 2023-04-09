import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
Ml = list(map(int,input().split()))

def binary_Search():
    for i in Ml:
        start = 0
        end = len(A)-1
        while True:
            mid = (start+end)//2
            if start >end:
                print(0)
                break
            if i == A[mid]:
                print(1)
                break
            elif i < A[mid]:
                end = mid-1
            elif i > A[mid]:
                start = mid+1

binary_Search()
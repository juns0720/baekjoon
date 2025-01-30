import sys
input = sys.stdin.readline




N,H = map(int,input().split())
even = []
odd = []
for i in range(N):
    if i % 2 == 0:
        even.append(int(input()))
    else:
        odd.append(int(input()))
even.sort()
odd.sort()
#s,e는 even 배열의 인덱스
def binary_search(arr,h):
    # 석순
    s = 0
    e = len(arr)
    while s < e:
        mid = (s + e) // 2
        if arr[mid] < h:
            s = mid + 1
        else:
            e = mid
    cnt = len(arr)-s
    return cnt

min_cnt = sys.maxsize
section_cnt = sys.maxsize
for h in range(1,H+1):
    cnt = binary_search(even,h+1) + binary_search(odd,H-h)
    if cnt < min_cnt:
        min_cnt = cnt
        section_cnt = 1
    elif cnt == min_cnt:
        section_cnt += 1

print(min_cnt, section_cnt) 

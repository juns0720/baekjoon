import sys
input = sys.stdin.readline

n, m = map(int, input().split())
titles = []

def binary_search(power):
    s, e = 0, len(titles)  # 반열린구간 사용 (e는 포함하지 않음)
    while s + 1 < e:  # s + 1 < e를 유지하여 반열린구간 방식 적용
        mid = (s + e) // 2
        if power <= titles[mid][1]:
            e = mid  # e를 mid로 변경하여 반열린구간 유지
        else:
            s = mid
    print(titles[s][0] if power <= titles[s][1] else titles[e][0])

for _ in range(n):
    a, b = input().strip().split()
    titles.append([a, int(b)])

for _ in range(m):
    power = int(input())
    binary_search(power)

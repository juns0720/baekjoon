import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())

arr = [input().strip() for _ in range(n)]
arr.sort()
items = Counter(arr)
print(items.most_common(n=1)[0][0])
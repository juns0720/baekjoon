import sys
input = sys.stdin.readline
Sum = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    Sum+=score
print(Sum//5)
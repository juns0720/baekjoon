import sys

input = sys.stdin.readline

n = int(input())
res = [0,0]

print(f"? 1\n")
sys.stdout.flush()
res[0] = int(input())

print(f"? {n}\n")
sys.stdout.flush()
res[1] = int(input())

ans = 0
if res[0] > res[1]:
    ans = -1
elif res[0] < res[1]:
    ans = 1

print(f"! {ans}")
sys.stdout.flush()

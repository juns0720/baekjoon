import sys
input = sys.stdin.readline


n = int(input())
key = input().strip()
cnt = 0
def check(s1, idx, interver, depth):
    global cnt

    if depth == len(key):
        cnt+=1
        return True
    
    for i in range(idx+1, len(s1)):
        if key[depth] == s1[i]:
            if depth == 1:
                if check(s1, i, i-idx, depth+1):
                    return True
            else:
                if interver == i-idx:
                    if check(s1,i,i-idx,depth+1):
                        return True



for _ in range(n):
    s1 = input().strip()
    for i in range(len(s1)):
        if s1[i] == key[0]:
            if check(s1, i, 0, 1):
                break

print(cnt)

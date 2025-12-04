import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
    exit()
    
cards = list(map(int,input().split()))
box = [0 for _ in range(10)]
cnt = 0

res = 0
for i in range(N-1):
    if box[cards[i]]:
        continue

    if cnt < 4:
        box[cards[i]] = 1
        cnt += 1
        res += 1

    else:
        least = cards[i+1:]

        tmp = []
        for j in range(len(box)):
            if box[j]:
                tmp.append(j)

        cand = []
        for c in tmp:
            for j in range(len(least)):
                if c == least[j]:
                    cand.append((c, j))
                    break
            else:
                box[c] = 0
                break
        else:
            cand.sort(key = lambda x: x[1])
            box[cand[-1][0]] = 0

        box[cards[i]] = 1
        res += 1

#마지막 카드 처리
if not box[cards[-1]]:
    res += 1
print(res)
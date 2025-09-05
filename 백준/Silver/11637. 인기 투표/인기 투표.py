import sys
input = sys.stdin.readline

for tc in range(int(input())):
    dic = dict()
    total = 0
    n = int(input())
    for i in range(n):
        a = int(input())
        total += a
        if a in dic:
            dic[a][0] += 1
            dic[a][1].append(i+1)
        else:
            dic[a] = [1,[i+1]]
    arr = sorted(list(dic.items()), key = lambda x : -x[0])
    if len(arr[0][1][1]) > 1:
        print("no winner")
    else:
        if arr[0][0] > total//2:
            print(f'majority winner {arr[0][1][1][0]}')
        else:
            print(f'minority winner {arr[0][1][1][0]}')
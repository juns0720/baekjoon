import sys
input = sys.stdin.readline

n = int(input())
flag2 = False
for i in range(2,11):
    tmp = []
    tmp_num = n

    while True:
        if tmp_num < i:
            tmp.append(str(tmp_num))
            break
        tmp.append(str(tmp_num % i))
        tmp_num//=i
    arr = ''.join(tmp)
    flag = True
    for j in range(len(tmp)//2):
        if arr[j] != arr[-j-1]:
            flag = False
            break
    if flag:
        flag2 = True
        print(i, arr)
if not flag2:
    print("NIE")
import sys
input = sys.stdin.readline

n_num = set(range(1,10001))     #그냥 자연수 1~10000
g_num = set()           #생성된 수
for i in range(1,10001):
    for j in str(i):        #i를 str()함수로 자릿수 분리
        i += int(j)     #j는 str이므로 int형으로 덧셈
    g_num.add(i)   

self_num = sorted(n_num-g_num)
for i in self_num:
    print(i)
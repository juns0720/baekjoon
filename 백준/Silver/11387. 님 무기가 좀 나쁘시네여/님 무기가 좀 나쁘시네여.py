import sys
input = sys.stdin.readline

cree = list(map(int,input().split()))
fabu = list(map(int,input().split()))
cree_w = list(map(int,input().split()))
fabu_w = list(map(int,input().split()))


def equip(p,w1,w2):
    for i in range(5):
        p[i]-=w1[i]
        p[i]+=w2[i]

def cal_cp(p):
    return p[0]*(100+p[1])*((10000-min(100*p[2],10000))+min(p[2],100)*p[3])*(100+p[4])

def print_res(prev,cur):
    if prev < cur:
        print('+')
    elif prev == cur:
        print('0')
    else:
        
        print('-')

prev_cree = cal_cp(cree)
equip(cree,cree_w,fabu_w)
cur_cree = cal_cp(cree)
print_res(prev_cree,cur_cree)

prev_fabu = cal_cp(fabu)
equip(fabu,fabu_w,cree_w)
cur_fabu = cal_cp(fabu)
print_res(prev_fabu,cur_fabu)




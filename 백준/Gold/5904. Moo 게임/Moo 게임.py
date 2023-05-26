import sys
input = sys.stdin.readline


def S(n,k,len):
    moo_len = len*2+(k+3)         
    if n < 4:
        if n == 1:
            print('m')
        else:
            print('o')
        return
         
    if n > moo_len:                         #길이 초과
        S(n,k+1,moo_len)
    else:                           
        if n > len and n <= len+(k+3):    # 센터에 있음
            if n == len+1:
                print('m')
            else:
                print('o')
        elif n > len+(k+3):               # 오른쪽에 있음
            want = n-(k+3)-len
            S(want,1,3)

n = int(input())
S(n,1,3)
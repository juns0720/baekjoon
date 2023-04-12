N = int(input())

s = '*'
for i in range(1,2*N):
    if i > N:
        for j in range(i-N,0,-1):
            print(' ',end='')
        print(s*(N*2-1-(i-N)*2))
    else:
        for j in range(N-i,0,-1):
            print(' ',end='')
        print(s*(2*i-1))
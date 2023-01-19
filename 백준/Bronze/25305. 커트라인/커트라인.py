import sys
input = sys.stdin.readline


#응시자 N명과 상을 받는 사람 K를 동시에 입력
p = list(map(int,input().split()))
score =  list(map(int,input().split()))

score.sort()

print(score[p[0]-p[1]])
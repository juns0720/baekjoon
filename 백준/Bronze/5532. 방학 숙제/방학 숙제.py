L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
korean = A//C +1
math = B//D +1
if A%C ==0:
    korean -=1
if B%D == 0:  
    math -=1

print(L-max(korean,math))
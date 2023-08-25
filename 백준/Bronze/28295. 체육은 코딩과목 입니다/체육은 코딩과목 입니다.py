arr = [0,0,0,0]
vec = ['N','E','S','W']
for i in range(10):
    arr[int(input())]+=1
Sum = arr[1]+arr[2]*2+arr[3]*(-1)
print(vec[Sum%4])
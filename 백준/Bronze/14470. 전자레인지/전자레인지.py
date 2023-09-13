arr = []
Sum = 0
for i in range(5):
    arr.append(int(input()))
if arr[0] < 0:
    Sum+=(-arr[0])*arr[2]
    Sum+=arr[3]
    Sum+=arr[4]*arr[1]
else:
    Sum+=arr[4]*(arr[1]-arr[0])
print(Sum)
import sys
from collections import deque



total_truck, len_bridge, max_weight = map(int,input().split())
trucks = list(map(int,input().split()))

bridge = deque([0 for _ in range(len_bridge)])

res, idx = 0, 0

while idx < total_truck:
    res += 1
    bridge.popleft()

    if sum(bridge) + trucks[idx] <= max_weight:
        bridge.append(trucks[idx])
        idx+=1
    else:
        bridge.append(0)

while bridge:
    res += 1
    bridge.popleft()

print(res)


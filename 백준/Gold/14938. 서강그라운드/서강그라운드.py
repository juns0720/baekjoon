import sys
import math
import heapq
input = sys.stdin.readline

total_node, search_range, total_edge = map(int,input().split())
item_costs = list(map(int,input().split()))
graph = [[] for _ in range(total_node+1)]
for i in range(total_edge):
    v1,v2,distance = map(int,input().split())
    graph[v1].append((v2,distance))
    graph[v2].append((v1,distance))

def dijkstra(start_node):
    hq = []
    heapq.heappush(hq,(0,start_node))

    while hq:
        corrent_dist, corrent_node = heapq.heappop(hq)

        if distance[corrent_node] < corrent_dist:
            continue

        for i in graph[corrent_node]:
            sum_distance = corrent_dist + i[1]
            if sum_distance < distance[i[0]]:
                distance[i[0]] = sum_distance
                heapq.heappush(hq, (sum_distance,i[0]))

def cal_distance(distance, search_range):
    total_item = 0
    for i in range(1, len(distance)):
        if distance[i] <= search_range:
            total_item+= item_costs[i-1]
    return total_item

max_total_item = 0

for start_node in range(1,total_node+1):
    distance = [math.inf for _ in range(total_node+1)]
    distance[start_node] = 0
    dijkstra(start_node)
    max_total_item = max(max_total_item, cal_distance(distance, search_range))
print(max_total_item)
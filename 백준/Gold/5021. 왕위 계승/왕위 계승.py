import sys
import heapq
input = sys.stdin.readline

gen = dict()
degree = dict()
dna = dict()

N, M = map(int,input().split())
king = input().strip()
dna[king] = 2**(N+1)

def init_parent_degree(parents):

    for parent in parents:
        if parent not in degree:
            degree[parent] = 0

def gen_graph(parents, child):
    if child not in gen:
        gen[child] = []

    for parent in parents:
        if parent not in gen:
            gen[parent] = [child]
        else:
            gen[parent].append(child)

def init_child_degree(child):
    if child not in degree:
        degree[child] = 2
    else:
        degree[child] += 2
        
for i in range(N):
    c,p1,p2 = list(input().split())

    init_parent_degree([p1,p2])

    gen_graph([p1,p2], c)

    init_child_degree(c)

hq = []
for name in degree.keys():
    if name not in dna:
        dna[name] = 0

    if degree[name] == 0:
        heapq.heappush(hq,name)


while hq:
    parent = heapq.heappop(hq)
    
    for child in gen[parent]:

        dna[child] += dna[parent] // 2

        degree[child] -= 1
        if degree[child] == 0:
            heapq.heappush(hq, child)

res = []
for i in range(M):
    name = input().strip()
    if name in dna:
        res.append((dna[name],name))

res.sort(key = lambda x: -x[0])
print(res[0][1])

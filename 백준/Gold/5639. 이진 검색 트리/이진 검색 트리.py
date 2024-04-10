import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

def postOrder(root, end):
    if root > end:
        return
    
    right = end+1

    for idx in range(root+1, end+1):
        if tree[root] < tree[idx]:
            right = idx
            break
    
    #왼쪽 탐색
    postOrder(root+1, right-1)
    
    #오른쪽 탐색
    postOrder(right, end)

    #탐색한 노드 출력
    print(tree[root])

postOrder(0, len(tree)-1)
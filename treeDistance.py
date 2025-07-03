import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(1 << 25)
n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

depth = [0] * (n + 1)
up = [0] * (n + 1)
ans = [0] * (n + 1)

stack = [(1, -1, 0)]
visited = [False] * (n + 1)
order = []

while stack:
    node, par, state = stack.pop()
    if state == 0:
        stack.append((node, par, 1))
        for nei in adj[node]:
            if nei != par:
                stack.append((nei, node, 0))
    else:
        d = 0
        for nei in adj[node]:
            if nei != par:
                d = max(d, 1 + depth[nei])
        depth[node] = d
from collections import deque
stack = deque()
stack.append((1, -1))

while stack:
    node, par = stack.popleft()

    children = [v for v in adj[node] if v != par]
    k = len(children)
    pre = [0] * (k + 2)
    suff = [0] * (k + 2)

    # Precompute prefix and suffix max of depths (excluding current child)
    for i in range(1, k + 1):
        pre[i] = max(pre[i - 1], 1 + depth[children[i - 1]])
    for i in range(k, 0, -1):
        suff[i] = max(suff[i + 1], 1 + depth[children[i - 1]])

    for i in range(k):
        child = children[i]
        best_other = max(pre[i], suff[i + 2])  # max of siblings excluding current
        up[child] = 1 + max(up[node], best_other)
        stack.append((child, node))
for i in range(1, n + 1):
    ans[i] = max(depth[i], up[i])

print(*ans[1:])


# import sys
# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# adj = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)

# def dfs_iterative(start):
#     dist = [-1] * (n + 1)
#     stack = [(start, 0)]
#     dist[start] = 0
#     while stack:
#         node, d = stack.pop()
#         for neighbor in adj[node]:
#             if dist[neighbor] == -1:
#                 dist[neighbor] = d + 1
#                 stack.append((neighbor, d + 1))
#     return dist
# dist1 = dfs_iterative(1)
# A = dist1.index(max(dist1))
# distA = dfs_iterative(A)
# B = distA.index(max(distA))
# distB = dfs_iterative(B)
# res = [max(distA[i], distB[i]) for i in range(1, n + 1)]
# print(*res)

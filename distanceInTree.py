import sys
input = lambda: sys.stdin.readline().rstrip()
n,k=map(int,input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

stack = []
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

stack.append((1, -1, 0)) 
vis = [False] * (n + 1)
vis[1] = True

while stack:
    node, par, state = stack.pop()
    if state == 0:
        stack.append((node, par, 1)) 
        for i in adj[node]:
            if i != par:
                vis[i] = True  
                stack.append((i, node, 0))
    else:
        for d in range(1, k + 1):
            for i in adj[node]:
                if i != par:
                    dp[node][d] += dp[i][d - 1]
from collections import deque

def reroot_iterative(n, k, adj, dp1):
    dp2 = [[0] * (k + 1) for _ in range(n + 1)]
    parent = [0] * (n + 1)
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
    for u in order:
        for d in range(k + 1):
            dp2[u][d] = dp1[u][d]

    for u in order[1:]:
        p = parent[u]
        dp2[u][1] += dp2[p][0]
        for d in range(2, k + 1):
            dp2[u][d] += dp2[p][d - 1]
            dp2[u][d] -= dp1[u][d - 2]

    return dp2
tot=0
ans=reroot_iterative(n,k,adj,dp)
for i in ans:
    tot+=i[-1]
print(tot//2)




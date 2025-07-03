n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [0] * (n+1)
sz = [1] * (n+1)
ans = [0] * (n+1)
# vis=[False]*(n+1)
# stack=[(1,-1,0)]
# vis[1]=True
# while stack:
#     node,par,state=stack.pop()
#     if not state:
#         state=1
#         stack.append((node,par,state))
#         for i in adj[node]:
#             if i==par:
#                 continue
#             if not vis[i]:
#                 vis[i]=True
#                 stack.append((i,node,0))
#     else:
#         for i in adj[node]:
#             if i==par:
#                 continue
#             sz[node]+=sz[i]
# vis1=[False]*(n+1)
# stack1=[(1,-1,0)]
# vis1[1]=True
# def dfs1(u, par):
#     for v in adj[u]:
#         if v != par:
#             dfs1(v, u)
#             # sz[u] += sz[v]
#             dp[u] += (dp[v]) + sz[v]
#     return dp[u]
stack = [(1, -1, 0)]

while stack:
    u, par, state = stack.pop()
    if state == 0:
        stack.append((u, par, 1))
        for v in adj[u]:
            if v != par:
                stack.append((v, u, 0))
    else:
        for v in adj[u]:
            if v != par:
                sz[u] += sz[v]
                dp[u] += dp[v] + sz[v]
# print(dp)
# def dfs2(u, par):
#     for v in adj[u]:
#         if v != par:
#             ans[v]=ans[u]+(n-sz[v])-(sz[v]) #ans[v]=ans[u]+(n-sz[v])-(dp[v]+sz[v])+dp[u] just think about this relationship you will get it
#             dfs2(v, u)
#     return ans[u]
from collections import deque
stack2=deque()
stack2.append((1,-1))
ans[1] = dp[1]
while stack2:
    node,par=stack2.popleft()
    for i in adj[node]:
        if i==par:
            continue
        ans[i]=ans[node]+(n-sz[i])-(sz[i]) 
        stack2.append((i,node))
        # print(i,sz[i],ans[node])
# print(dp)
print(*ans[1:])

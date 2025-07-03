# import sys
# input = lambda: sys.stdin.readline().rstrip()
# it = lambda: int(input())
# maa = lambda: map(int, input().split())
# lis = lambda: list(maa())

# n = it()
# adj=[[] for _ in range(n+1)]
# for _ in range(n-1):
#     a,b=maa()
#     adj[a].append(b)
#     adj[b].append(a)
# dp=[-1]*(n+1)
# maxi=0
# def f(i,par):
#     global maxi
#     s=[]
#     for j in adj[i]:
#         if j==par:
#            continue
#         s.append(f(j,i))
#     s.sort()
#     if len(s)>=2:
#         maxi=max(maxi,s[-1]+s[-2])
#     elif len(s)==1:
#         maxi=max(maxi,s[-1])
    

#     return 1+(s[-1] if s else 0)
# f(1,-1)
# print(maxi)

import sys
input = lambda: sys.stdin.readline().rstrip()
it = lambda: int(input())
maa = lambda: map(int, input().split())
lis = lambda: list(maa())

sys.setrecursionlimit(1 << 25)

n = it()
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = maa()
    adj[a].append(b)
    adj[b].append(a)

depth = [0] * (n + 1)
visited = [False] * (n + 1)
maxi = 0

stack = [(1, -1, 0)]  # (node, parent, state), state=0 for pre-processing, 1 for post-processing
post = []

while stack:
    node, par, state = stack.pop()
    if state == 0:
        visited[node] = True
        stack.append((node, par, 1))  # post-processing after children
        for nei in adj[node]:
            if nei != par and not visited[nei]:
                stack.append((nei, node, 0))
    else:
        s = []
        for nei in adj[node]:
            if nei != par:
                s.append(depth[nei])

        s.sort()
        if len(s) >= 2:
            maxi = max(maxi, s[-1] + s[-2])
        elif len(s) == 1:
            maxi = max(maxi, s[0])

        depth[node] = 1 + (s[-1] if s else 0)

print(maxi)

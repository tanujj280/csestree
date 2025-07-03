# import sys
# input = lambda: sys.stdin.readline().rstrip()
# n = int(input())
# adj = [[] for _ in range(n + 1)]

# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)

# dp = [[0, 0] for _ in range(n + 1)]
# parent = [-1] * (n + 1)

# stack = [(1, False)]

# while stack:
#     u, visited = stack.pop()

#     if not visited:
#         stack.append((u, True))
#         for v in adj[u]:
#             if v != parent[u]:
#                 parent[v] = u
#                 stack.append((v, False))
#     else:
#         for v in adj[u]:
#             if v == parent[u]:
#                 continue
#             dp[u][0] += max(dp[v][0], dp[v][1])

#         for v in adj[u]:
#             if v == parent[u]:
#                 continue
#             candidate = dp[u][0] - max(dp[v][0], dp[v][1]) + dp[v][0] + 1
#             dp[u][1] = max(dp[u][1], candidate)

# print(max(dp[1][0], dp[1][1]))



import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]
parent = [-1] * (n + 1)

def f(i,par):
    s=0
    for j in adj[i]:
        if j==par:
           continue
        s+=f(j,i)
    dp[i][0]=s
    maxi=0
    for j in adj[i]:
        if j==par:
            continue
        maxi=max(maxi,1+s-max(dp[j][0],dp[j][1])+dp[j][0])
    dp[i][1]=maxi

    return max(dp[i][0],dp[i][1])
print(f(1,-1))


    
    


       



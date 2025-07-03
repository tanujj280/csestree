import sys
input = lambda: sys.stdin.readline().rstrip()
it = lambda: int(input())
maa = lambda: map(int, input().split())
lis = lambda: list(maa())

n = it()
a=lis()
adj=[[] for _ in range(n+1)]
for i in range(n-1):
    adj[a[i]].append(i+2)
dp=[-1]*(n+1)
# def dfs(i):
#     if dp[i] != -1:
#         return dp[i]
    
#     len =0
#     for ni in adj[i]:
#         # print(ni,i)
#         len+=(1+dfs(ni))
        
#     dp[i]=len
#     return dp[i]
# dfs(1)  
stack = [(1, False)]
while stack:
    node, visited = stack.pop()
    if not visited:
        stack.append((node, True))
        for child in adj[node]:
            if dp[child] == -1:
                stack.append((child, False))
    else:
        total = 0
        for child in adj[node]:
            total += 1 + dp[child]
        dp[node] = total

print(*dp[1:])
    


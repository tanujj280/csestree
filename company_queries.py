# n,q=map(int,input().split())
# a=list(map(int,input().split()))
# adj=[[] for _ in range(n+1)]
# for i in range(len(a)):
#     adj[a[i]].append(i+2)
# import math
# log=math.floor(math.log2(n)) + 1
# up=[[-1]*log for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in adj[i]:
#         up[j][0]=i
# for i in range(1,log):
#     for j in range(1,n+1):
#         if up[j][i-1]!=-1:
#             up[j][i]=up[up[j][i-1]][i-1]
# def get_kth_ancestor(node, k):
#     for i in range(log):
#         if k & (1 << i):
#             node = up[node][i]
#             if node == -1:
#                 return -1
#     return node

# for _ in range(q):
#     node, k = map(int, input().split())
#     print(get_kth_ancestor(node, k))

import sys
import math

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, q = map(int, input[ptr:ptr+2])
    ptr +=2
    a = list(map(int, input[ptr:ptr+n-1]))
    ptr +=n-1

    adj = [[] for _ in range(n+1)]
    for i in range(len(a)):
        adj[a[i]].append(i+2)

    log_max = math.floor(math.log2(n)) + 1
    up = [[-1]*(log_max) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in adj[i]:
            up[j][0] = i

    for i in range(1, log_max):
        for j in range(1, n+1):
            if up[j][i-1] != -1:
                up[j][i] = up[up[j][i-1]][i-1]

    output = []
    for _ in range(q):
        node, k = map(int, input[ptr:ptr+2])
        ptr +=2
        current = node
        for i in range(log_max):
            if k & (1 << i):
                current = up[current][i]
                if current == -1:
                    break
        output.append(str(current))

    print('\n'.join(output))

if __name__ == '__main__':
    main()
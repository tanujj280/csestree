// import sys
// input = lambda: sys.stdin.readline().rstrip()
// from collections import deque
// import math
// n,q=map(int,input().split())
// adj = [[] for _ in range(n + 1)]

// for _ in range(n - 1):
//     u, v = map(int, input().split())
//     adj[u].append(v)
//     adj[v].append(u)

// stack = deque()
// log_max = math.floor(math.log2(n)) + 1
// up = [[-1]*(log_max) for _ in range(n+1)]
// dpth = [0 for _ in range(n + 1)]

// stack.append((1,0,0)) 

// while stack:
//     node,level,par= stack.popleft()
//     for i in adj[node]:
//         if i != par:
//             up[i][0]=node
//             stack.append((i,level+1,node))
//             dpth[i]=level+1
// for i in range(1, log_max):
//     for j in range(1, n+1):
//         if up[j][i-1] != -1:
//             up[j][i] = up[up[j][i-1]][i-1]
// # output=[]
// for _ in range(q):
//     a,b=map(int,input().split())   
//     def lca(u,v):
//         if dpth[u] < dpth[v]: u,v=v,u
//         # // Bring u up to depth of v
//         for k in range(log_max-1,-1,-1):
//             if (dpth[u] - (1 << k) >= dpth[v]):
//                 u = up[u][k]
    
//         if (u == v):return u
//         for k in range(log_max-1,-1,-1):
//             if (up[u][k] != -1 and up[u][k] != up[v][k]):
//                 u = up[u][k]
//                 v = up[v][k]
//         return up[u][0]

//     node=lca(a,b)
//     print(dpth[a]+dpth[b]-2*dpth[node])
//     # output.append((dpth[a]+dpth[b]-2*dpth[node],node,dpth[node]))
// # print(output)

        

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    int log_max = floor(log2(n)) + 1;
    vector<vector<int>> up(n + 1, vector<int>(log_max, -1));
    vector<int> dpth(n + 1, 0);
    
    deque<tuple<int, int, int>> stack;
    stack.push_back({1, 0, 0});
    
    while (!stack.empty()) {
        auto [node, level, par] = stack.front();
        stack.pop_front();
        
        for (int i : adj[node]) {
            if (i != par) {
                up[i][0] = node;
                dpth[i] = level + 1;
                stack.push_back({i, level + 1, node});
            }
        }
    }
    
    for (int i = 1; i < log_max; i++) {
        for (int j = 1; j <= n; j++) {
            if (up[j][i - 1] != -1) {
                up[j][i] = up[up[j][i - 1]][i - 1];
            }
        }
    }
    
    auto lca = [&](int u, int v) {
        if (dpth[u] < dpth[v]) swap(u, v);
        
        for (int k = log_max - 1; k >= 0; k--) {
            if (dpth[u] - (1 << k) >= dpth[v]) {
                u = up[u][k];
            }
        }
        
        if (u == v) return u;
        
        for (int k = log_max - 1; k >= 0; k--) {
            if (up[u][k] != -1 && up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }
        return up[u][0];
    };
    
    while (q--) {
        int a, b;
        cin >> a >> b;
        int node = lca(a, b);
        cout << dpth[a] + dpth[b] - 2 * dpth[node] << '\n';
    }
    
    return 0;
}
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

vector<vector<int>> adj;
vector<vector<int>> up;
vector<int> depth;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    adj.resize(n + 1);
    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
        adj[i].push_back(p);
    }

    int LOG = log2(n) + 1;
    up.assign(n + 1, vector<int>(LOG, -1));
    depth.resize(n + 1);

    // BFS to compute depth and immediate parents (up[i][0])
    queue<int> qu;
    qu.push(1);
    up[1][0] = -1;  // Root has no parent
    depth[1] = 0;
    while (!qu.empty()) {
        int u = qu.front();
        qu.pop();
        for (int v : adj[u]) {
            if (v != up[u][0]) {  // Avoid going back to parent
                up[v][0] = u;
                depth[v] = depth[u] + 1;
                qu.push(v);
            }
        }
    }

    // Binary Lifting DP
    for (int k = 1; k < LOG; ++k) {
        for (int v = 1; v <= n; ++v) {
            if (up[v][k - 1] != -1) {
                up[v][k] = up[up[v][k - 1]][k - 1];
            }
        }
    }

    // LCA function
    auto lca = [&](int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        // Bring u up to depth of v
        for (int k = LOG - 1; k >= 0; --k) {
            if (depth[u] - (1 << k) >= depth[v]) {
                u = up[u][k];
            }
        }
        if (u == v) return u;
        // Now find LCA
        for (int k = LOG - 1; k >= 0; --k) {
            if (up[u][k] != -1 && up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }
        return up[u][0];
    };

    // Process queries
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }

    return 0;
}

def dfs(node, visited, graph):
    """DFS for finding reflextion of a mirror using dynamic programming"""
    memo = {}
    MOD = 10**9 + 7

    if node in visited:
        return 0
    if node in memo:
        return memo[node]
    if len(graph[node]) == 0:
        return 1

    total = 0
    visited.add(node)
    for next_node in graph[node]:
        total = (total + dfs(next_node, visited, graph)) % MOD
    visited.remove(node)

    memo[node] = total
    return total

def main():
    """Main function"""
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        tokens = list(map(int, input().split()))
        k = tokens[0]
        if k > 0:
            graph[i] = tokens[1:]
        else:
            graph[i] = []
    print(dfs(1, set(), graph))

main()

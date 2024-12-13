from collections import defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    manager = int(input())
    def dfs(node, parent, message_state):
        max_users = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                if message_state == 0 or (message_state == -1 and neighbor > node) or (message_state == 1 and neighbor < node):
                    new_state = 0 if message_state != 0 else (neighbor - node)
                    max_users = max(max_users, 1 + dfs(neighbor, node, new_state))
        return max_users
    return dfs(manager, -1, 0)

if __name__ == '__main__':
    print(main())

def dfs_tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    path = []
    min_cost = float('inf')
    best_path = []

    def dfs(current, cost, count):
        nonlocal min_cost, best_path

        if count == n and graph[current][start] > 0:
            total_cost = cost + graph[current][start]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [start]
            return

        for next_city in range(n):
            if not visited[next_city] and graph[current][next_city] > 0:
                visited[next_city] = True
                path.append(next_city)
                dfs(next_city, cost + graph[current][next_city], count + 1)
                visited[next_city] = False
                path.pop()

    visited[start] = True
    path.append(start)
    dfs(start, 0, 1)
    return min_cost, best_path

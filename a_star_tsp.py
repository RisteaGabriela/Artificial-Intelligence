import heapq


def a_star_tsp(graph, start):
    n = len(graph)

    def heuristic(path):
        remaining = set(range(n)) - set(path)
        return min(graph[path[-1]][city] for city in remaining) if remaining else 0

    pq = [(0 + heuristic([start]), 0, start, [start])]
    min_cost = float('inf')
    best_path = []

    while pq:
        est_cost, cost, current, path = heapq.heappop(pq)
        if len(path) == n:
            if graph[current][start] > 0:
                total_cost = cost + graph[current][start]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path + [start]
        for next_city in range(n):
            if next_city not in path and graph[current][next_city] > 0:
                new_path = path + [next_city]
                heapq.heappush(pq, (
                    cost + graph[current][next_city] + heuristic(new_path), cost + graph[current][next_city], next_city,
                    new_path))

    return min_cost, best_path

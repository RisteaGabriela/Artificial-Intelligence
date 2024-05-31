import heapq


def uniform_cost_tsp(graph, start):
    n = len(graph)
    pq = [(0, start, [start])]
    min_cost = float('inf')
    best_path = []

    while pq:
        cost, current, path = heapq.heappop(pq)
        if len(path) == n:
            if graph[current][start] > 0:
                total_cost = cost + graph[current][start]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path + [start]
        for next_city in range(n):
            if next_city not in path and graph[current][next_city] > 0:
                heapq.heappush(pq, (cost + graph[current][next_city], next_city, path + [next_city]))

    return min_cost, best_path

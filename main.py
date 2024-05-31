import time
from a_star_tsp import a_star_tsp
from data_generater import generate_random_distance_matrix, read_distance_matrix
from dfs_tsp import dfs_tsp
from uniform_cost_tsp import uniform_cost_tsp

if __name__ == '__main__':
    n = 8  # Number of cities
    max_distance = 700  # Maximum distance between cities
    filename = 'input5.txt'
    # generate_random_distance_matrix(n, max_distance, filename)

    # Verify the generated matrix by reading it
    graph = read_distance_matrix(filename)
    print(graph)

    # Measure runtime of DFS TSP
    start_time = time.perf_counter()
    dfs_result = dfs_tsp(graph, 0)
    dfs_runtime = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds

    # Measure runtime of Uniform Cost TSP
    start_time = time.perf_counter()
    uniform_cost_result = uniform_cost_tsp(graph, 0)
    uniform_cost_runtime = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds

    # Measure runtime of A* TSP
    start_time = time.perf_counter()
    a_star_result = a_star_tsp(graph, 0)
    a_star_runtime = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds

    print(f"DFS TSP Result: {dfs_result}, Runtime: {dfs_runtime:.6f} ms")
    print(f"Uniform Cost TSP Result: {uniform_cost_result}, Runtime: {uniform_cost_runtime:.6f} ms")
    print(f"A* TSP Result: {a_star_result}, Runtime: {a_star_runtime:.6f} ms")

    # Save results to a text file
    with open('results.txt', 'a') as results_file:
        results_file.write("Input5:\n")
        results_file.write("DFS TSP Result:\n")
        results_file.write(f"Path: {dfs_result[1]}\n")
        results_file.write(f"Cost: {dfs_result[0]}\n")
        results_file.write(f"Runtime: {dfs_runtime:.6f} ms\n\n")

        results_file.write("Uniform Cost TSP Result:\n")
        results_file.write(f"Path: {uniform_cost_result[1]}\n")
        results_file.write(f"Cost: {uniform_cost_result[0]}\n")
        results_file.write(f"Runtime: {uniform_cost_runtime:.6f} ms\n\n")

        results_file.write("A* TSP Result:\n")
        results_file.write(f"Path: {a_star_result[1]}\n")
        results_file.write(f"Cost: {a_star_result[0]}\n")
        results_file.write(f"Runtime: {a_star_runtime:.6f} ms\n\n")

    print("Results have been saved to results.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

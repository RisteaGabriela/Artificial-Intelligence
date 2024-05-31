import random


def generate_random_distance_matrix(n, max_distance, filename):

    distance_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            distance = random.randint(1, max_distance)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    with open(filename, 'w') as file:
        for row in distance_matrix:
            file.write(' '.join(map(str, row)) + '\n')


def read_distance_matrix(filename):

    distance_matrix = []

    with open(filename, 'r') as file:
        for line in file:
            # Split the line into individual distances and convert them to integers
            row = list(map(int, line.split()))
            distance_matrix.append(row)

    return distance_matrix

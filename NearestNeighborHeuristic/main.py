import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def nearest_neighbor(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    total_distance = 0
    current = 0

    for _ in range(n - 1):
        nearest, nearest_dist = None, float('inf')
        for i in range(n):
            if not visited[i]:
                d = distance(cities[current], cities[i])
                if d < nearest_dist:
                    nearest, nearest_dist = i, d
        tour.append(nearest)
        visited[nearest] = True
        total_distance += nearest_dist
        current = nearest

    total_distance += distance(cities[current], cities[0])
    tour.append(0)
    return tour, total_distance

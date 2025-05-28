import random
import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def create_tour(n):
    tour = list(range(n))
    random.shuffle(tour)
    return tour + [tour[0]]

def total_tour_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def crossover(p1, p2):
    size = len(p1) - 1
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[start:end] = p1[start:end]
    p2_filtered = [city for city in p2 if city not in child]
    j = 0
    for i in range(size):
        if child[i] == -1:
            child[i] = p2_filtered[j]
            j += 1
    return child + [child[0]]

def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(cities, population_size=50, generations=500):
    n = len(cities)
    population = [create_tour(n) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda tour: total_tour_distance(tour, cities))
        next_gen = population[:10]  # elite selection

        while len(next_gen) < population_size:
            parents = random.sample(population[:25], 2)
            child = crossover(parents[0], parents[1])
            mutate(child)
            next_gen.append(child)

        population = next_gen

    best = min(population, key=lambda tour: total_tour_distance(tour, cities))
    return best, total_tour_distance(best, cities)

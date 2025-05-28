import random
import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def total_tour_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(cities, temp=1000.0, cooling_rate=0.995, stop_temp=1e-3):
    n = len(cities)
    current_tour = list(range(n)) + [0]
    current_cost = total_tour_distance(current_tour, cities)

    while temp > stop_temp:
        i, j = sorted(random.sample(range(1, n), 2))
        new_tour = current_tour[:]
        new_tour[i:j] = reversed(new_tour[i:j])
        new_cost = total_tour_distance(new_tour, cities)
        delta = new_cost - current_cost

        if delta < 0 or math.exp(-delta / temp) > random.random():
            current_tour = new_tour
            current_cost = new_cost

        temp *= cooling_rate

    return current_tour, current_cost

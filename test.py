from GeneticAlgorithmHeuristic.main import genetic_algorithm
from NearestNeighborHeuristic.main import nearest_neighbor
from SimulatedAnnealingHeuristic.main import simulated_annealing


if __name__ == "__main__":
    cities = [
        (0, 0), (10, 10), (20, 5), (15, 25), (5, 20),
        (25, 15), (30, 30), (12, 0), (8, 18), (3, 7)
    ]

    print("Nearest Neighbor:")
    nn_tour, nn_cost = nearest_neighbor(cities)
    print("Tour:", nn_tour)
    print("Cost:", round(nn_cost, 2), "\n")

    print("Simulated Annealing:")
    sa_tour, sa_cost = simulated_annealing(cities)
    print("Tour:", sa_tour)
    print("Cost:", round(sa_cost, 2), "\n")

    print("Genetic Algorithm:")
    ga_tour, ga_cost = genetic_algorithm(cities)
    print("Tour:", ga_tour)
    print("Cost:", round(ga_cost, 2))

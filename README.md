# Heuristic Algorithms for the Traveling Salesman Problem (TSP)

This repository provides clean and practical implementations of three well-known heuristic algorithms to approximate solutions for the **Traveling Salesman Problem (TSP)**:

- Nearest Neighbor Algorithm
- Simulated Annealing
- Genetic Algorithm

These algorithms are implemented in pure Python using only the standard library, and can be executed on hardcoded city coordinates to demonstrate their comparative performance and solution quality.

## Problem Definition

The Traveling Salesman Problem (TSP) is a classic combinatorial optimization problem defined as follows:

> Given a list of cities and the distances between each pair of cities, determine the shortest possible route that visits each city exactly once and returns to the starting city.

TSP is known to be NP-hard, meaning no polynomial-time algorithm is known to solve all instances optimally. As such, heuristic and metaheuristic approaches are often used to find near-optimal solutions in reasonable time for practical problems.

---

## Algorithm Descriptions

### 1. Nearest Neighbor Algorithm

**Category:** Greedy Heuristic  
**Complexity:** O(n²)

**Overview:**  
The Nearest Neighbor algorithm builds a tour by always moving to the closest unvisited city. It starts from a randomly chosen city and continues until all cities have been visited, at which point it returns to the starting city to complete the cycle.

**Procedure:**
1. Select an initial city arbitrarily.
2. From the current city, select the nearest unvisited city and travel there.
3. Repeat step 2 until all cities have been visited.
4. Return to the starting city.

**Advantages:**
- Very fast and easy to implement.
- Useful as a baseline for comparison.

**Disadvantages:**
- Often produces suboptimal results.
- Greedy nature may lead to poor decisions early on that cannot be corrected.

---

### 2. Simulated Annealing

**Category:** Metaheuristic, Probabilistic Optimization  
**Complexity:** Depends on the cooling schedule and number of iterations

**Overview:**  
Simulated Annealing is inspired by the physical process of annealing in metallurgy. It explores the solution space by probabilistically accepting both improvements and certain degradations in solution quality to avoid local minima.

**Procedure:**
1. Start with an initial solution (a random tour).
2. Repeat:
   - Generate a new candidate tour by swapping two cities.
   - Compute the difference in tour lengths.
   - If the new tour is shorter, accept it.
   - If the new tour is longer, accept it with a probability that decreases over time (`exp(-Δ/T)`).
3. Gradually reduce the temperature `T` (cooling schedule).
4. Stop when the system is “frozen” (temperature is low enough or no improvements are found).

**Key Parameters:**
- Initial temperature (controls how often worse solutions are accepted initially).
- Cooling rate (determines how quickly the algorithm becomes conservative).
- Iterations per temperature level.

**Advantages:**
- Capable of escaping local optima.
- Simple and general-purpose.

**Disadvantages:**
- Requires careful tuning of parameters.
- May be slower than greedy methods.

---

### 3. Genetic Algorithm

**Category:** Evolutionary Algorithm  
**Complexity:** O(generations × population_size × evaluation_cost)

**Overview:**  
Genetic Algorithms simulate natural selection and evolution. A population of candidate solutions is evolved over several generations using operations such as selection, crossover (recombination), and mutation.

**Procedure:**
1. Initialize a population of random tours.
2. Evaluate each tour’s fitness (inverse of the total distance).
3. Select a subset of the best-performing tours (elitism).
4. Create new tours by recombining pairs of parents (crossover).
5. Occasionally mutate some offspring by swapping cities.
6. Repeat steps 2–5 for a fixed number of generations.
7. Return the best tour found.

**Key Components:**
- **Selection:** Retain top-performing individuals for the next generation.
- **Crossover:** Combine subpaths of two parents to create a new child tour.
- **Mutation:** Introduce small random changes to avoid premature convergence.

**Advantages:**
- Scalable and powerful for large search spaces.
- Performs well across a wide range of TSP instances.

**Disadvantages:**
- Requires tuning of population size, mutation rate, etc.
- Computationally more expensive than other heuristics.

---

## File Overview

- `main.py`: Main script that defines cities and runs all three algorithms.
- `nearest_neighbor.py`: Contains implementation of the greedy nearest neighbor heuristic.
- `simulated_annealing.py`: Implementation of the simulated annealing algorithm.
- `genetic_algorithm.py`: Implements genetic operations including selection, crossover, and mutation.

---

## Usage

To run the program with hardcoded city data:

```bash
python main.py

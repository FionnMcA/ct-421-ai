import itertools
import os
import time
from utils import read_tsp_as_dict, create_distance_matrix, genome_distance

# Brute-force to find the best route
def brute_force_tsp(city_dict, distance_matrix):
    start = time.time()
    cities = list(city_dict.keys())
    best_route = None
    best_distance = float("inf")
    # Generate all permutations of the cities
    for permutation in itertools.permutations(cities):
        distance = genome_distance(permutation, distance_matrix)
        if distance < best_distance:
            best_distance = distance
            best_route = permutation
    end = time.time()
    duration = end - start
    return best_route, best_distance, duration

filepath = os.path.join("tsp-files", "test11.tsp")
city_dict = read_tsp_as_dict(filepath)

distance_matrix = create_distance_matrix(city_dict)

best_route, best_distance, duration = brute_force_tsp(city_dict, distance_matrix)

print("City Dictionary:", city_dict)
print("Optimal Route:", best_route)
print("Optimal Distance:", best_distance)
print("Brute force duration:", duration)
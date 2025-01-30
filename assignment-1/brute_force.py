import itertools
from utils import read_tsp_as_dict, create_distance_matrix, genome_distance

# Brute-force to find the best route
def brute_force_tsp(city_dict, distance_matrix):
    cities = list(city_dict.keys())
    best_route = None
    best_distance = float("inf")
    # Generate all permutations of the cities
    for permutation in itertools.permutations(cities):
        distance = genome_distance(permutation, distance_matrix)
        if distance < best_distance:
            best_distance = distance
            best_route = permutation
    return best_route, best_distance


city_dict = read_tsp_as_dict("/Users/fionnmcardle/Desktop/assignments/ct-421-ai/assignment-1/tsp-files/test5.tsp")

distance_matrix = create_distance_matrix(city_dict)

best_route, best_distance = brute_force_tsp(city_dict, distance_matrix)

print("City Dictionary:", city_dict)
print("Optimal Route:", best_route)
print("Optimal Distance:", best_distance)
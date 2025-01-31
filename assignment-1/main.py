import time
import random
import os
from operators import cycle_crossover, ordered_crossover, swap_mutation, scramble_mutation
from utils import read_tsp_as_dict, init_population, create_distance_matrix, genome_distance, fitnesses, select_parent


def genetic_algorithm(filepath, generations=100, population_size=100, mutation_rate=0.02, crossover_rate=0.8):
    start = time.time() # Start the timer
    city_dict = read_tsp_as_dict(filepath) # Convert the file to a dictionary

    population = init_population(population_size, len(city_dict)) # Initialize a random population

    best_distances = []
    average_distances = []

    distance_matrix = create_distance_matrix(city_dict) # Create the distance matrix

    overall_best_genome = None
    overall_best_distance = float('inf')

    for generation in range(generations):

        pop_distances = [genome_distance(genome, distance_matrix) for genome in population] # Get the distance of each genome

        pop_fitnesses = fitnesses(pop_distances) # Get the fitness of each genome

        new_population = []

        for _ in range(population_size // 2):
            # select two random parents
            parent1 = select_parent(population, pop_fitnesses)
            parent2 = select_parent(population, pop_fitnesses)

            # Crossover
            if random.random() < crossover_rate:
                if random.random() < 0.5:
                    offspring1, offspring2 = cycle_crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = ordered_crossover(parent2, parent1)
            else:
                offspring1, offspring2 = parent1[:], parent2[:]

            if random.random() < mutation_rate:
                if random.random() < 0.5:
                    offspring1 = swap_mutation(offspring1)
                else:
                    offspring1 = scramble_mutation(offspring1)

            # Mutation
            if random.random() < mutation_rate:
                if random.random() < 0.5:
                    offspring2 = swap_mutation(offspring2)
                else:
                    offspring2 = scramble_mutation(offspring2)

            new_population.extend([offspring1, offspring2])

        # Calculate the generation's stats
        best_index = pop_fitnesses.index(population_size)
        best_in_pop = population[best_index]
        best_distance_in_pop = pop_distances[best_index]
        best_distances.append(best_distance_in_pop)
        average_distances.append(sum(pop_distances) / len(pop_distances))

        if best_distance_in_pop < overall_best_distance:
            overall_best_distance = best_distance_in_pop
            overall_best_genome = best_in_pop

        population = new_population

    # End the timer
    end = time.time()
    duration = end - start

    return duration, best_distances, average_distances, overall_best_genome, overall_best_distance


def main():
    files = ['test5', 'test10', 'berlin52', 'kroA100', 'pr1002']
    for file in files:
        filepath = os.path.join("tsp-files", f"{file}.tsp")
        duration, best_distances, average_distances, overall_best_genome, overall_best_distance = genetic_algorithm(filepath, 200, 500, 0.02, 0.8)
        print(f"{file} - duration: {duration} - best distance: {overall_best_distance} ")

if __name__ == "__main__":
    main()

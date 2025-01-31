import math
import random

def read_tsp_as_dict(filepath):
    """
    Reads a .tsp file and converts it into a dictionary.
    Returns a dictionary of cities indexed by their ID with (x, y) coordinates.
    """
    city_dict = {}
    node_coord_section = False  # Correctly track when to start parsing

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith("NODE_COORD_SECTION"):
                node_coord_section = True
                continue

            if line == "EOF":
                break

            if node_coord_section:
                parts = line.split()
                if len(parts) >= 3:
                    index = int(parts[0])  # City index
                    x, y = float(parts[1]), float(parts[2])  # City coordinates
                    city_dict[index] = (x, y)

    return city_dict


def euclidean_distance(city1, city2):
    """
    Calculates and returns the Euclidean distance between two cities
    """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def create_distance_matrix(city_dict):
    """
    A method to produce a distance matrix where the distance between
    each city is calculated and stored in a (symmetrical) matrix
    This prevents the program from having to compute the same distance calculations over and over
    """
    dimension = len(city_dict)
    distance_matrix = [[0] * dimension for _ in range(dimension)]
    for i in range(1, dimension + 1):
        for j in range(i+1, dimension +1):
            distance = euclidean_distance(city_dict[i], city_dict[j])
            distance_matrix[i-1][j-1] = distance
            distance_matrix[j-1][i-1] = distance
    return distance_matrix


def genome_distance(genome, distance_matrix):
    """
    Calculate the total distance travelled in the solution
    """
    distance = 0
    n = len(genome)
    for i in range(n):
        current_city = genome[i] - 1
        next_city = genome[(i + 1) % n] - 1
        distance += distance_matrix[current_city][next_city]
    return distance


def random_genome(length):
    """
    Creates a random genome of numbers from 1 to length inclusive,
    where each number represents the city index
    """
    numbers = list(range(1, length + 1))
    random.shuffle(numbers)
    return numbers


def init_population(population_size, genome_length):
    """
    Creates a population of random genomes
    """
    return [random_genome(genome_length) for _ in range(population_size)]


def fitnesses(distances):
    """
    Takes in a list of distances and assigns each distance a rank, where the shorter
    the distance the higher the rank
    Then returns a list of fitness values corresponding to the order of the inputted list
    """
    # Sorts indices so shortest distance gets highest rank
    sorted_indices = sorted(range(len(distances)), key=lambda k: distances[k])

    ranks = [0] * len(distances)
    for rank, index in enumerate(sorted_indices):
        ranks[index] = len(distances) - rank
    return ranks # List of ranks corresponding to population order

def select_parent(population, population_fitness):
    """
    Randomly selects a few genomes from the population
    the best genome is chosen to be returned (Tournament Selection)
    """
    pop_size = len(population)
    num_contestants = round(pop_size * 0.25)

    tournament_indices = random.sample(range(len(population)), num_contestants)

    # Gets the index of the best chosen indice based on their fitness
    # best_index = max(tournament_indices, key=lambda k: population_fitness[k])
    tournament_fitness = [population_fitness[i] for i in tournament_indices]
    best_index = tournament_indices[max(range(len(tournament_fitness)), key=lambda i: tournament_fitness[i])]

    return population[best_index]
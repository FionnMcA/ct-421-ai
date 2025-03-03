import random
from strategy import Strategy


def init_population(population_size):
    return [random_genome(i) for i in range(population_size)]

def random_genome(name):
    first_move = random.choice([0, 1])
    # friedman = random.choice([True,False])
    responses = {
        (1,): random.choice([0, 1]),
        (0,): random.choice([0, 1]),
        (1, 1): random.choice([0, 1]),
        (1, 0): random.choice([0, 1]),
        (0, 1): random.choice([0, 1]),
        (0, 0): random.choice([0, 1]),
    }
    random_strat = Strategy(name=f"Random Strategy - {name}", first_move=first_move, responses=responses, memory_size=2)
    # print(f" first_move - {first_move} - responses {responses}")
    return random_strat

def fitnesses(scores):
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return sorted_indices

def select_parent(population, population_fitness):
    pop_size = len(population)
    num_contestants = round(pop_size * 0.25)

    tournament_indices = random.sample(range(pop_size), num_contestants)

    tournament_fitness = [population_fitness[i] for i in tournament_indices]
    best_index = tournament_fitness.index(max(tournament_fitness))

    return population[best_index]

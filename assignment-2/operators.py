import random
from strategy import Strategy

def mutation(strategy, mutation_rate=0.5):
    first_move = strategy.first_move if random.random() > mutation_rate else random.choice([0, 1])

    response_map = {
        key: val if random.random() > mutation_rate else random.choice([0, 1])
        for key, val in strategy.responses.items()
    }

    return Strategy(name="", first_move=first_move, responses=response_map, memory_size=2)

def crossover(parent1, parent2):
    off_1_first_move = random.choice([parent1.first_move, parent2.first_move])
    off_2_first_move = random.choice([parent1.first_move, parent2.first_move])

    off_1_map = {key: random.choice([parent1.responses[key], parent2.responses[key]]) for key in parent1.responses}
    off_2_map = {key: random.choice([parent1.responses[key], parent2.responses[key]]) for key in parent1.responses}

    return (
        Strategy(name="", first_move=off_1_first_move, responses=off_1_map, memory_size=2),
        Strategy(name="", first_move=off_2_first_move, responses=off_2_map, memory_size=2)
    )

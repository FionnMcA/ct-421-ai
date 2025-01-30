import random

def ordered_crossover(parent1, parent2):
    """
    Takes a random subsequence from each parent
    Copies the subsequence into the corresponding child
    Then starting from the right of the subsequence fill in the remaining
    positions in each child with genes from the other parent in the order
    they appear, starting from the right of the subsequence
    """
    size = len(parent1)
    child1 = [None] * size
    child2 = [None] * size

    # Get a random start and end cut points
    start, end = sorted(random.sample(range(size), 2))

    # Copy the subsequence from the parents to the corresponding childs
    child1[start:end] = parent1[start:end]
    child2[start:end] = parent2[start:end]

    pos1 = end
    pos2 = end

    # Fill in the remaining genes
    for gene in parent2[end:] + parent2[:end]:
        if gene not in child1:
            while child1[pos1] is not None:
                pos1 = (pos1+1)%size
            child1[pos1] = gene
    for gene in parent1[end:] + parent1[:end]:
        if gene not in child2:
            while child2[pos2] is not None:
                pos2 = (pos2+1)%size
            child2[pos2] = gene

    return child1, child2

def cycle_crossover(parent1, parent2):
    """
    Follow the gene mappings to form a cycle, copying these genes into the corresponding child
    Then fill in the remaining positions in each child with genes from the other parent
    """
    size = len(parent1)
    child1 = [None] * size
    child2 = [None] * size

    visited = [False] * size

    # Start of the cycle
    index = 0
    while not visited[index]:
        visited[index] = True
        # Copy the cycle from parent1 to child1
        child1[index] = parent1[index]
        # Copy the cycle from parent2 to child2
        child2[index] = parent2[index]
        next_val = parent2[index]
        index = parent1.index(next_val)

    # Fill in the remaining blanks from the other parent
    for i in range(size):
        if child1[i] is None:
            child1[i] = parent2[i]
        if child2[i] is None:
            child2[i] = parent1[i]

    return child1, child2

def swap_mutation(genome):
    """
    Swaps two random positions in the genome
    """
    size = len(genome)
    swap1, swap2 = random.sample(range(size), 2)
    genome[swap1], genome[swap2] = genome[swap2], genome[swap1]
    return genome

def scramble_mutation(parent):
    """
    Takes a random subsequence of the genome and shuffle the order of it
    """
    size = len(parent)
    start, end = sorted(random.sample(range(size), 2))
    subset = parent[start:end + 1]
    random.shuffle(subset)
    mutated = parent[:start] + subset + parent[end + 1:]
    return mutated

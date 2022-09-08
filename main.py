from deap import creator, base, tools, algorithms
from numpy import matrix
from getSequences import getSequences
import random
from objectiveFunction import evaluate
from population import generateSeqList, normalizeSize

sequences = []

def generate_individual():
    return sequences

NUMSEQUENCES = 3
POPSIZE = 10

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)

#getting initial population
sequences = generateSeqList(sequences, NUMSEQUENCES)
sequences = normalizeSize(sequences)

#starting genetic algorithm
#maximizing problem
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

#generating populations
toolbox = base.Toolbox()
toolbox.register("sequences", generate_individual)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.sequences)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
pop = toolbox.population(n=POPSIZE)

#adding objective function
toolbox.register("evaluate", evaluate)

CXPB, MUTPB, NGEN = 0.5, 0.2, 40

fitnesses = map(toolbox.evaluate, pop)
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

for g in range(NGEN):
    # Select the next generation individuals
    offspring = toolbox.select(pop, len(pop))
    # Clone the selected individuals
    offspring = map(toolbox.clone, offspring)

    # Apply crossover and mutation on the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # The population is entirely replaced by the offspring
    pop[:] = offspring

print(pop)
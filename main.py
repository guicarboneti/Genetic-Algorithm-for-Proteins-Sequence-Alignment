from deap import creator, base, tools, algorithms
from numpy import matrix
from getSequences import getSequences
import random
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
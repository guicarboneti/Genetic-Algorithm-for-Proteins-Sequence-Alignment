from ctypes import alignment
from deap import creator, base, tools, algorithms
from numpy import matrix
from getSequences import getSequences
import random
from population import generateSeqList, normalizeSize

NUMSEQUENCES = 3
POPSIZE = 10

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)

#getting initial population
sequences = generateSeqList(sequences, NUMSEQUENCES)
sequences = normalizeSize(sequences)
population = []
for i in range(POPSIZE):
    alignment = {
        "alignment": sequences,
        "score": 0,
        "expectedOffspring": 0
    }
    population.append(alignment)

#starting genetic algorithm
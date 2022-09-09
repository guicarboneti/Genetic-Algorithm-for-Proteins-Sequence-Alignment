from fileinput import close
import poplib
from deap import creator, base, tools, algorithms
from numpy import matrix
from getSequences import getSequences
import random
from objectiveFunction import evaluate
from operators import generateInitialIndividual
from population import generateSeqList, normalizeSize

NUMSEQUENCES = 3
NUMGENERATIONS = 40
POPSIZE = 10

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)

#getting initial population
sequences = generateSeqList(sequences, NUMSEQUENCES)
sequences = normalizeSize(sequences)
pop = []

for i in range(POPSIZE):
    individual = {
        "alingment": generateInitialIndividual(sequences),
        "score": 0,
        "expectedOffspring": 0
    }
    pop.append(individual)
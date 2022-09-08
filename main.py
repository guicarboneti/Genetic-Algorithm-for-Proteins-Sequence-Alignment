import poplib
from deap import creator, base, tools, algorithms
from numpy import matrix
from getSequences import getSequences
import random
from objectiveFunction import evaluate
from operators import crossover, gapInsertion, gapShift, sequenceShift
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
pop = []

for i in range(POPSIZE):
    pop.append(sequences)
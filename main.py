from deap import creator, base, tools, algorithms
from getSequences import getSequences
import random

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)
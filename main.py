from deap import creator, base, tools, algorithms
from numpy import matrix
from getSequences import getSequences
import random
from pam250 import pam250

PAM250 = pam250.matrix

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)
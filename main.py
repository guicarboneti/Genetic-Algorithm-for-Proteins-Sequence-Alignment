from fileinput import close
from deap import creator, base, tools, algorithms
from numpy import matrix, sort
from getSequences import getSequences
import random
from objectiveFunction import evaluate
from operators import generateInitialIndividual, newChild
from population import generateSeqList, normalizeSize, toList

NUMSEQUENCES = 3
NUMGENERATIONS = 15
POPSIZE = 4

def scoreKey(e):
    return e["score"]

def printPopulation(pop):
    algNumber = 1
    for i in pop:
        print("Alinhamento", algNumber)
        alignment = []
        for j in i['alignment']:
            sequence = ''
            sequence = sequence.join(j)
            alignment.append(sequence)

        print(alignment)
        print("Score:", str(i['score']))
        algNumber = algNumber + 1

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)

#getting initial population
sequences = generateSeqList(sequences, NUMSEQUENCES)
sequences = normalizeSize(sequences)
sequences = toList(sequences)
pop = []

for i in range(POPSIZE):
    individual = {
        "alignment": generateInitialIndividual(sequences),
        "score": 0
    }
    pop.append(individual)

for i in range(NUMGENERATIONS):
    print("Geração", i + 1)
    for individual in pop:
        if individual["score"] == 0:
            individual["score"] = evaluate(individual["alignment"])

    pop.sort(key=scoreKey)

    # remove the worst half
    for individual in range(len(pop) // 2):
        pop.remove(pop[individual])

    # generate new children
    parents = pop.copy()
    for j in range(len(pop) // 2):
        parent1 = random.choice(parents)
        parents.remove(parent1)
        parent2 = random.choice(parents)
        parents.append(parent1)

        child = {
            "alignment": newChild(parent1, parent2),
            "score": 0
        }
    
        pop.append(child)

# end of genetic algorithm
for individual in pop:
        if individual["score"] == 0:
            individual["score"] = evaluate(individual["alignment"])

printPopulation(pop)
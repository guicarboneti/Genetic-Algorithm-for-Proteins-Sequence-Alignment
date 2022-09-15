import statistics
from getSequences import getSequences
from utils import *
import random
from objectiveFunction import evaluate
from operators import generateInitialIndividual, newChild
from population import generateSeqList, normalizeSize, toList

NUMSEQUENCES = 3
NUMGENERATIONS = 200
POPSIZE = 15
CXPB = 0.5
MTPB = 0.2

def scoreKey(e):
    return e["score"]

def printPopulation(pop):
    alignmentFile = open("alignment.txt", "w")
    algNumber = 1
    for i in pop:
        print("Alinhamento", algNumber, file=alignmentFile)
        alignment = []
        for j in i['alignment']:
            sequence = ''
            sequence = sequence.join(j)
            alignment.append(sequence)

        print(alignment, file=alignmentFile)
        print("Score:", str(i['score']), file=alignmentFile)
        algNumber = algNumber + 1
    alignmentFile.close()

#getting list of sequences
sequences = getSequences()

#shuffling list
random.shuffle(sequences)

resultfile = open("result.csv", "w")
print("generation,highest_fitness,average_fitness,standard_deviation", file=resultfile)

#getting initial population
sequences = generateSeqList(sequences, NUMSEQUENCES)
sequences = normalizeSize(sequences)
sequences = toList(sequences)

pop = []

for i in range(POPSIZE):
    individual = {
        "alignment": ListOfCharsToString(generateInitialIndividual(sequences)),
        "score": 0
    }
    pop.append(individual)

# retransform into list of chars
for ind in pop:
    ind["alignment"] = (toList(strToListOfChars(ind["alignment"])))

# compute fitness of population 0
for individual in pop:
    individual["score"] = evaluate(individual["alignment"])

for i in range(NUMGENERATIONS):
    print("Geração", i)

    # SELECTION (remove the worst half)
    pop.sort(key=scoreKey)
    for individual in range(POPSIZE // 2):
        pop.remove(pop[individual])

    # CROSSOVER
    parents = pop.copy()
    for j in range(POPSIZE // 2):
        parent1 = random.choice(parents)
        parents.remove(parent1)
        parent2 = random.choice(parents)
        parents.append(parent1)

        child = {
            "alignment": newChild(parent1, parent2, CXPB, MTPB),
            "score": 0
        }
    
        pop.append(child)

    # compute fitness of population
    for individual in pop:
            individual["score"] = evaluate(individual["alignment"])

    popScores = [i['score'] for i in pop]
    print(i, ",", max(popScores), ",", sum(popScores) / len(popScores), ",", statistics.pstdev(popScores), file=resultfile) 

# end of genetic algorithm
for individual in pop:
        if individual["score"] == 0:
            individual["score"] = evaluate(individual["alignment"])

print(NUMGENERATIONS, ",", max(popScores), ",", sum(popScores) / len(popScores), ",", statistics.pstdev(popScores), file=resultfile) 

resultfile.close()

# printPopulation(pop)
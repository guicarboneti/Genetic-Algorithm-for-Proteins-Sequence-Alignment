import random
from objectiveFunction import evaluate

# makes a crossover of two alignments
def crossover(parentAlg1, parentAlg2):
    alg1 = parentAlg1.copy()
    alg2 = parentAlg2.copy()
    indexStart = random.randrange(len(alg1[0]))

    for i in range(len(alg1)):
        for j in range(indexStart, indexStart + random.randrange(1, len(alg1[0]) - indexStart)):
            temp = alg1[i][j]
            alg1[i][j] = alg2[i][j]
            alg2[i][j] = temp

    # return the one that scores better
    if evaluate(alg1) > evaluate(alg2):
        return alg1
    else:
        return alg2

# inserts 1 to 4 gaps in each sequence
def gapInsertion(parentAlg):
    alg = parentAlg.copy()

    for i in alg:
        for times in range(4):
            i.insert(random.randrange(len(i)), '-')

    return alg

# shifts one gap in one sequence to the left
def gapShiftLeft(parentAlg):
    alg = parentAlg.copy()
    sequence = random.choice(alg)
    index = alg.index(sequence)

    if not '-' in sequence:
        return gapInsertion(parentAlg)

    gapindexes = [i for i,val in enumerate(sequence) if val=='-']

    i = random.choice(gapindexes)

    temp = sequence[i - 1]
    sequence[i - 1] = sequence[i]
    sequence[i] = temp
    alg[index] = sequence

    return alg

# shifts one gap in one sequence to the right
def gapShiftRight(parentAlg):
    alg = parentAlg.copy()
    sequence = random.choice(alg)
    index = alg.index(sequence)

    if not '-' in sequence:
        return gapInsertion(parentAlg)

    gapindexes = [i for i,val in enumerate(sequence) if val=='-']

    i = random.choice(gapindexes)

    if (len(sequence) <= i + 1):
        gapShiftLeft(parentAlg)

    temp = sequence[i + 1]
    sequence[i + 1] = sequence[i]
    sequence[i] = temp
    alg[index] = sequence

    return alg

def generateInitialIndividual(parentAlg):
    operators = [gapInsertion, gapShiftLeft]

    return random.choice(operators)(parentAlg)

def newChild(parent1, parent2):
    operators = [gapInsertion, gapShiftLeft, crossover, gapShiftRight]

    chosenOperator = random.choice(operators)

    if chosenOperator == crossover:
        return chosenOperator(parent1["alignment"], parent2["alignment"])
    else:
        return chosenOperator(parent1["alignment"])
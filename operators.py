import random
from objectiveFunction import evaluate

# makes a crossover of two alignments
def crossover(parentAlg1, parentAlg2):
    alg1 = parentAlg1.copy()
    alg2 = parentAlg2.copy()
    indexStart = random.randrange(0, len(alg1[0])-11)

    for i in range(len(alg1)):
        temp = alg2[i][indexStart:indexStart+10]
        alg2[i] = alg2[i].replace(temp, alg1[i][indexStart:indexStart+10])
        alg1[i] = alg1[i].replace(alg1[i][indexStart:indexStart+10], temp)

    # return the one that scores better
    if evaluate(alg1) > evaluate(alg2):
        return alg1
    else:
        return alg2

# inserts 1 gap in each sequence
def gapInsertion(parentAlg):
    alg = []

    for i in parentAlg:

        index1 = random.randrange(0, len(parentAlg[0]))
        index2 = random.randrange(0, len(parentAlg[0]))

        for i in range(0, len(parentAlg)//2):
            alg.append(parentAlg[i][:index1] + '-' + parentAlg[i][index1:])

        for i in range(len(parentAlg)//2 + 1, len(parentAlg)):
            alg.append(parentAlg[i][:index2] + '-' + parentAlg[i][index2:])

    return alg

# shifts sequences a random number of letters
def alignmentShift(parentAlg):
    alg = []
    for i in parentAlg:
        r_rot = random.randrange(5, 15)
        l_rot = random.randrange(5,15)
            
        alg.append((i * 3)[len(i) + r_rot - l_rot : 2 * len(i) + r_rot - l_rot])

    return alg

# shifts one gap in one sequence to the left
def gapShiftLeft(parentAlg):
    sequence = random.randrange(len(parentAlg))
    sequence = parentAlg[sequence]
    if not '-' in sequence:
        return parentAlg

    try:
        index = [i for i in range(len(sequence)) if sequence.startswith('-', i)]
        index = index[random.randrange(len(index))]
    except:
        return parentAlg

    alg = []
    for i in parentAlg:
        if i == sequence:
            alg.append(sequence.replace(sequence[index - 1] + sequence[index], sequence[index] + sequence[index - 1]))
        else:
            alg.append(i)
        
    return alg

# shifts one gap in one sequence to the right
def gapShiftRight(parentAlg):
    sequence = random.randrange(len(parentAlg))
    sequence = parentAlg[sequence]
    if not '-' in sequence:
        return parentAlg
    index = [i for i in range(len(sequence)) if sequence.startswith('-', i)]
    index = index[random.randrange(len(index) - 1)]

    alg = []
    for i in parentAlg:
        if i == sequence:
            alg.append(sequence.replace(sequence[index] + sequence[index + 1] , sequence[index + 1]  + sequence[index]))
        else:
            alg.append(i)
        
    return alg

def generateInitialIndividual(parentAlg):
    operators = [gapInsertion, alignmentShift, gapShiftLeft]

    return random.choice(operators)(parentAlg)

def newChild(parent1, parent2):
    operators = [gapInsertion, gapShiftLeft, alignmentShift, crossover, gapShiftRight]

    chosenOperator = random.choice(operators)

    if chosenOperator == crossover:
        return chosenOperator(parent1["alignment"], parent2["alignment"])
    else:
        return chosenOperator(parent1["alignment"])
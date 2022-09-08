import random

# makes a crossover of two alignments
def crossover(parentAlg1, parentAlg2):
    alg1 = parentAlg1
    alg2 = parentAlg2
    indexStart = random.randrange(0, len(alg1[0]))
    indexEnd = random.randrange(indexStart+1, len(alg1[0]))

    for i in range(len(alg1)):
        temp = alg2[i][indexStart:indexEnd]
        alg2[i] = alg2[i].replace(temp, alg1[i][indexStart:indexEnd])
        alg1[i] = alg1[i].replace(alg1[i][indexStart:indexEnd], temp)

    # return one that scores better
    return alg1

# inserts one gap
def gapInsertion(parentAlg):
    alg = []
    index1 = random.randrange(0, len(parentAlg[0]))
    index2 = random.randrange(0, len(parentAlg[0]))

    for i in range(0, len(parentAlg)//2):
        alg.append(parentAlg[i][:index1] + '-' + parentAlg[i][index1:])

    for i in range(len(parentAlg)//2 + 1, len(parentAlg)):
        alg.append(parentAlg[i][:index2] + '-' + parentAlg[i][index2:])

    return alg

# shifts the whole alignment a random number of letters
def alignmentShift(parentAlg):
    alg = []
    for i in parentAlg:
        r_rot = random.randrange(5, 15)
        l_rot = random.randrange(5,15)
        
        alg.append((i * 3)[len(i) + r_rot - l_rot : 2 * len(i) + r_rot - l_rot])

    return alg

# shifts one gap in one sequence to the left or to the right
def gapShift(parentAlg):
    sequence = random.randrange(len(parentAlg))
    sequence = parentAlg[sequence]
    index = [i for i in range(len(sequence)) if sequence.startswith('-', i)]

    index = index[random.randrange(len(index))]

    alg1 = []
    for i in parentAlg:
        if i == sequence:
            alg1.append(sequence.replace(sequence[index] + sequence[index + 1], sequence[index + 1] + sequence[index]))
        else:
            alg1.append(i)

    alg2 = []
    for i in parentAlg:
        if i == sequence:
            alg2.append(sequence.replace(sequence[index - 1] + sequence[index], sequence[index] + sequence[index - 1]))
        else:
            alg2.append(i)
    
    # return the one with the best score
    return alg2
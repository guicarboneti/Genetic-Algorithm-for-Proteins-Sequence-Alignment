def generateSeqList(sequences, popSize):
    seqList = []
    for i in range(0, popSize):
        seqList.append(sequences[i])
    return seqList

def normalizeSize(sequences):
    newLen = len(max(sequences, key=len))

    newSequences = []

    for i in sequences:
        while len(i) < newLen:
            i = i + '-'
        newSequences.append(i)
    
    return newSequences

def toList(sequences):
    newSequences = []

    for i in sequences:
        newSequences.append([*i])

    return newSequences
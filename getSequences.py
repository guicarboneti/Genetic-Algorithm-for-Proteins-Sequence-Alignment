def getSequences():
    file = open('sequences/seqdump.txt')
    lines = file.readlines()

    sequences = []
    newSequence = ''

    for line in lines:
        if line[0] == '>' and line != lines[0]:
            sequences.append(newSequence.replace('\n', ''))
            newSequence = ''
        elif line != lines[0]:
            newSequence = newSequence + line
    
    return sequences
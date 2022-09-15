from pam250 import pam250
from skbio import *

PAM250 = pam250.matrix

def pairScore(seq1, seq2):
    sum = 0
    for i in range(len(seq1)):
        sum = sum + int(PAM250[str(seq1[i])][str(seq2[i])]) + 8
    return sum

def buildGuideTree(dMatrix):
    dm = DistanceMatrix(dMatrix)
    tree = nj(dm).root_at_midpoint()
    return tree

def calculateWeights(gTree):
    n = gTree.count(tips=True)
    weights = []
    for i in range(n):
        w = 0
        t = gTree.find(str(i))
        while not t.is_root():
            w = w + t.length / (max(1,t.count(tips=True)))
            t = t.parent
        weights.append(w)
    return weights

def normalize(w):
    max_val = max(w)
    for i in range(len(w)):
        w[i] = w[i] / max_val

def evaluate(alignment):
    score = 0
    distanceMatrix = [[0 for x in range(len(alignment))] for y in range(len(alignment))]
    score_arr = []
    for i in range(len(alignment)):
        j = i + 1
        while j < len(alignment):
            partialScore = pairScore(alignment[i], alignment[j])
            distanceMatrix[i][j] = partialScore
            distanceMatrix[j][i] = partialScore
            score_arr.append(partialScore)
            j = j + 1
    guideTree = buildGuideTree(distanceMatrix)
    w = calculateWeights(guideTree)
    normalize(w)
    for i in range(len(alignment)):
        score = score + w[i] * score_arr[i]
    return score
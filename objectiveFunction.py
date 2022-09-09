from pam250 import pam250
PAM250 = pam250.matrix

def pairScore(seq1, seq2):
    sum = 0
    for i in range(len(seq1)):
        sum = sum + PAM250[seq1[i]][seq2[i]]
    return sum

def evaluate(alignment):
    score = 0
    for i in range(len(alignment)):
        j = i + 1
        while j < len(alignment):
            score = score + pairScore(alignment[i], alignment[j])
            j = j + 1
    return score
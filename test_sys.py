from random import randint
import random
import numpy as np

perfect_genes = [0]*500

def flip_value(value, lst_of_indices):
    for i in range(1, len(value)+1):
        if i in lst_of_indices:
            if value[i-1] == 0:
                value[i-1] = 1
            else:
                value[i-1] = 0
    return value

def calfitness(genes1):
    return np.sum(genes1 == perfect_genes).astype(float)
from random import randint
import random


perfect = [1]*500
# fitness = 2

def flip_value(value, lst_of_indices):
    for i in range(1, len(value)+1):
        if i in lst_of_indices:
            if value[i-1] == 0:
                value[i-1] = 1
            else:
                value[i-1] = 0
    return value

def calfitness(value, lst_of_indices):
    value = flip_value(value, lst_of_indices)

    fitness = 0
    for i in range(len(value)):
        if value[i] == perfect[i]:
            fitness += 1
    return value, fitness

# while True:
#     inp = input()
#     lst_of_indices = [int(inputt) for inputt in inp.split()]
#     value , fitness = calfitness(value, lst_of_indices)
#     print('fitness: ', fitness)
#     print('value: ', value)
# # calfitness(, [1,2,3])
# print('hi')
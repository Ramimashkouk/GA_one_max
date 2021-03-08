from random import randint 
import random
import numpy as np

class Individual:
    def __init__(self, individual_length):
        self.genes = np.empty(individual_length, int)
        for i in range(individual_length):
            self.genes[i] = randint(0,1)
    def set_fitness(self, fitness):
        self.fitness = fitness


    def mate(self, partner):
        child = Individual(len(self.genes))

        crosspoint = randint(0, len(self.genes)-1)
        for i in range(len(self.genes)):
            if i > crosspoint:
                child.genes[i] = partner.genes[i]
            else:
                child.genes[i] = self.genes[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.uniform(0,1) < mutation_rate:
                if self.genes[i] == 0:
                    self.genes[i] = 1
                else:
                    self.genes[i] = 0
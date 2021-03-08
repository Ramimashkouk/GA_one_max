from individual import Individual
from test_sys import calfitness
from random import randint
import random

value = [1]*500

class Population:
    def __init__(self, individual_length, mutation_rate, max_populationation):
        self.individual_length = individual_length
        self.mutation_rate = mutation_rate
        self.max_populationation = max_populationation

        self.population = []
        for _ in range(max_populationation):
            self.population.append(Individual(individual_length))

        self.generations = 1
        self.finished = False
        
    def get_fitness(self): 
        for i in range(len(self.population)):
            fitness = calfitness(self.population[i].genes)
            if fitness == self.individual_length:
                self.finished = True
            
            fitness = 2** fitness 
            fitness = fitness * 100 / 2 ** self.individual_length
            self.population[i].set_fitness(fitness)
        
        self.max_fitness = max([ind.fitness for ind in self.population])
        
        fitness_sum = sum([ind.fitness for ind in self.population])
        self.probabilities = [ind.fitness / fitness_sum for ind in self.population]
        
    def go_and_fuck(self):
        new_population = []
        for _ in range(len(self.population)):
            partner1 = self.accept_reject()
            partner2 = self.accept_reject()
            child = partner1.mate(partner2)
            child.mutate(self.mutation_rate)
            new_population.append(child)

        self.population = new_population
        self.generations += 1

    def accept_reject(self):
        index = -1
        rand = random.uniform(0, 1)

        while rand > 0:
            index += 1
            rand -= self.probabilities[index]
        return self.population[index]

    def get_best(self):
        return self.max_fitness
    
    def display(self):
        for ind in self.population[0:25]:
            individual_in_string = ''
            for element in ind.genes:
                individual_in_string += str(element)
            print(individual_in_string)
       
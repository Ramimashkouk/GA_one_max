from random import randint
import random
import time
from test_sys import calfitness

value = [1]*100 + [0]*400
queries = 0

class Population:
    def __init__(self, individual_length, mutation_rate, max_populationation):
        self.individual_length = individual_length
        self.mutation_rate = mutation_rate
        self.max_populationation = max_populationation

        self.population = []
        for _ in range(max_populationation):
            self.population.append(Individual(individual_length))

        self.mating_pool = []
        self.generations = 1

    def get_fitness(self, last_individual): #here last individual means the one with 
                                        #last query 
        global value    
        global queries
        for i in range(len(self.population)):
            different_genes_indices = self.population[i].compare_genes(last_individual)
            
            # for j in range(i):
            #     if self.population[i].genes == self.population[j].genes:
            #         self.population[i].fitness = self.population[j].fitness
            # take into consideration that in case something was found the same
            # there's no need for inputing 

            if len(different_genes_indices) != 0 :
                value , fitness = calfitness(value, different_genes_indices)
                queries += 1
                # print()
                # fitness = int(input())                    
                if fitness == self.individual_length:
                    print('\nSolution found')
                    return True
            # and queries <= (3*self.individual_length)/4 +99
            # elif queries > (3*self.individual_length)/4 +99:
            #     print(queries)
            #     return False
            else:
                fitness = last_individual.fitness
            fitness = 2 ** fitness 
            fitness = fitness * 100 / 2 ** self.individual_length 
            self.population[i].set_fitness(fitness)
            last_individual = self.population[i]
        return last_individual

    def natural_selection(self):
        self.mating_pool =[]
        maxfitness = max([ind.fitness for ind in self.population])
        for ind in self.population:
            # if maxfitness == 0: maxfitness = 1
            fitness = int(ind.fitness * 100 / maxfitness)
            self.mating_pool += [ind]* fitness

    def go_and_fuck(self):
        for i in range(len(self.population)):
            partner1 = self.mating_pool[randint(0, len(self.mating_pool)-1)]
            partner2 = self.mating_pool[randint(0, len(self.mating_pool)-1)]
            child = partner1.mate(partner2)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generations += 1

    def get_best(self):
        return max([ind.fitness for ind in self.population])
    
    def display(self):
        for ind in self.population[0:25]:
            individual_in_string = ''
            for element in ind.genes:
                individual_in_string += str(element)
            print(individual_in_string)
        

class Individual:
    def __init__(self, individual_length):
        self.genes = []
        for _ in range(individual_length):
            self.genes.append(randint(0,1))
    def set_fitness(self, fitness):
        self.fitness = fitness

    def compare_genes(self, individual):
        different_genes_indices = []
        for i in range(len(self.genes)):
            if self.genes[i] != individual.genes[i]:
                different_genes_indices.append(i)
        return [element+1 for element in different_genes_indices]

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

inp = input()
start_time = time.time()
target_length = int(inp.split()[0])
first_fitness = int(inp.split()[1])
mutation_rate = 0.009
max_populationation = 800 # it should depend on target_length I think

first_individual = Individual(target_length)
first_individual.set_fitness(first_fitness)

population = Population(target_length, mutation_rate, max_populationation)
last_individual = population.get_fitness(first_individual)

while True:
    # if we found the last individual with perfect genes break!
    if last_individual == True:
        break
    if last_individual == False:
        print('Queries exeeded')
        break
    print(time.time() - start_time)
    print('Generation number: ', population.generations)
    print('Best fitness: ', population.get_best(), ' %', '\n')

    #display the population
    # population.display()

    #fill the mating pool
    population.natural_selection()

    #generate new generation
    population.go_and_fuck()

    #get fitnesses for the new generation
    last_individual = population.get_fitness(last_individual)


print(time.time() - start_time)
print(queries)
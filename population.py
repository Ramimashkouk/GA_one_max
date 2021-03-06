from individual import Individual
from test_sys import calfitness
from random import randint

value = [1]*100
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
       
import time
from population import Population, queries
from individual import Individual

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
# print(queries)
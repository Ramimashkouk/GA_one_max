import time
from population import Population
from individual import Individual

inp = input()
start_time = time.time()
target_length = int(inp.split()[0])
first_fitness = int(inp.split()[1])
mutation_rate = 0.009
max_populationation = 600 # it should depend on target_length I think

population = Population(target_length, mutation_rate, max_populationation)
population.get_fitness()

while True:
    if population.finished:
        break

    print(time.time() - start_time)
    print('Generation number: ', population.generations)
    print('Best fitness: ', population.get_best(), ' %', '\n')

    #display the population
    # population.display()

    #generate new generation
    population.go_and_fuck()

    #get fitnesses for the new generation
    population.get_fitness()

print(time.time() - start_time)
# print(queries)
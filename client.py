import numpy
import ga
import sys
num_weights = 11
sol_per_pop = 8
num_parents_mating = 4

pop_size = (sol_per_pop,num_weights)
def mutator(new_population,size,new_size):
    new_one=[]
    new_one.append(new_population[0]) 
    for x in range(1,new_size):
        fake=[]
        for x in range(0,11):
            fake.append(new_population[0][x])
        index=numpy.random.randint(low=0,high=size)
        opening=0.9*fake[index]
        end =1.1* fake[index]
        random_value = numpy.random.uniform(opening,end)   
        while random_value >=10 or random_value <=-10:
            index+=1
            index=index%x
        opening=0.9*fake[index]
        end =1.1*fake[index]
        random_value = numpy.random.uniform(opening,end)
        fake[index]=random_value
        new_one.append(fake)
    return new_one

new_population=[[10.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]]
new_population=mutator(new_population,11,8)
new_population=numpy.array(new_population)
print(new_population)
num_generations = 10
for generation in range(num_generations):
    print("Generation : ", generation)
    fitness = ga.cal_pop_fitness(new_population)
    parents = ga.select_mating_pool(new_population, fitness, 
                                      num_parents_mating)
    print("parents",parents,"\n")
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(4, num_weights))
    print("offspring_crossover",offspring_crossover,"\n")
    offspring_mutation = ga.mutation(offspring_crossover,generation)
    print("offspring_mutation",offspring_mutation,"\n")
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation
fitness = ga.cal_pop_fitness(new_population)
print(fitness)
best_match_idx = numpy.where(fitness == numpy.min(fitness))
print("best_match_idx",best_match_idx[0][0])
print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx[0][0]])
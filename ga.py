import numpy
import requests
import json
import random
infinity=float('inf')
def cal_pop_fitness(pop):
    error=[]
    for x in range(len(pop)):
        err = get_errors('fiP6JijQ2GF3yWtdOuTfzQkibcpBC4azI3ad0cJaLRqW7MyW3m',list(pop[x]))
        submit_status = submit('fiP6JijQ2GF3yWtdOuTfzQkibcpBC4azI3ad0cJaLRqW7MyW3m', list(pop[x]))
        combined=(0.4)* err[0]+(0.6)* err[1]
        error.append(combined)
        # print(err[1])
    return error

def select_mating_pool(pop, fitness, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.min(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = infinity
    return parents

def crossover(parents,offspring_size):
    offspring=numpy.empty(offspring_size)
    for k in range(offspring_size[0]):
        for l in range(offspring_size[1]):
            value=random.choice([0,1])
            if value==0:
                value1=k%parents.shape[0]
                offspring[k][l] = parents[value1][l]
            else:
                value1=(k+1)%parents.shape[0]
                offspring[k][l] = parents[value1][l]
    return offspring

def mutation(offspring_crossover,generation):
    for idx in range(offspring_crossover.shape[0]):
        index=numpy.random.randint(low=1,high=offspring_crossover.shape[1])
        opening=0.9*offspring_crossover[idx,index]
        end =1.1* offspring_crossover[idx,index] 
        random_value = numpy.random.uniform(opening,end)   
        while random_value >=10 or random_value <=-10:
            index+=1
            index=index%11
        opening=0.9*offspring_crossover[idx,index]
        end =1.1* offspring_crossover[idx,index]
        random_value = numpy.random.uniform(opening,end)   
        offspring_crossover[idx,index] =random_value
    return offspring_crossover


######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11

# functions that you can call
def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector:
        assert -10 <= abs(i) <= 10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))


def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector:
        assert -10 <= abs(i) <= 10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

# utility functions


def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path:
        root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root


def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id': id, 'vector': vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response

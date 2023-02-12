# Import Libraries
import numpy as np
import pandas as pd
import random


# Inputs of the Parameters
"""
The S=target is to maximize this equation ASAP:
    S=100-(((n-na)(100-h))/D)
    where (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)=(12.7,10.5,15.71,19.62,13.65,14.4,15.26,4.87,18.13,17.28,15.66)
    where (na1,na2,na3,na4,na5,na6,na7,na8,na9,na10,na11)=(12.46,10.23,15.10,15.6,3.9,11.9,11.2,3.8,11.8,9.5,8.4)
    where (h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11)=(60,60,30,35,30,30,40,40,30,30,30)
    where (D1,D2,D3,D4,D4,D5,D6,D7,D8,D9,D10,D11)=(300,300,1500,1000,600,960,240,2000,400,300,400)/(1.38, 2.83, 12.31, 22.8, 16.25, 20.16, 6.5, 18.5, 10.91, 8.34, 11.05)
    What are the best values for S?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""


# Creating the Initial Population
pop_size = 30

new_population1 = np.random.uniform(low=4.0, high=19.62, size=pop_size)
df1 = pd.DataFrame(new_population1, columns=['efficiency_inputs'])
new_population2 = np.random.uniform(low=3.8, high=15.6, size=pop_size)
df2 = pd.DataFrame(new_population2, columns=['efficiency_aged_inputs'])
new_population3 = np.random.randint(low=30, high=60, size=pop_size)      
df3 = pd.DataFrame(new_population3, columns=['humidity_inputs'])
new_population4 = np.random.uniform(low=1.38, high=22.8, size=pop_size)
df4 = pd.DataFrame(new_population4, columns=['duration_inputs'])

population = np.array([df1, df2, df3, df4])
n_pop = np.round(population, 2)
new_pop = n_pop.transpose()
new_population=np.reshape(new_pop,(pop_size,4))

valid_pop = []
for i in range(pop_size):
    if new_population[i][0] > new_population[i][1]:
        valid_pop.append(new_population[i])

X = np.array(valid_pop)
print(X)


# Measuring the Fitness Value of each chromosome in the population
for num in range(1):

   efficiency_inputs = new_population1
   efficiency_aged_inputs = new_population2
   humidity_inputs = new_population3
   duration_inputs = new_population4
      
   fv = (100-(((efficiency_inputs-efficiency_aged_inputs)*(100-humidity_inputs))/duration_inputs))
   fitness_value = np.round(fv, 2)
   fitness_value_2d = fitness_value.reshape(-1, 1)
   print("Fitness Value:\n", fitness_value_2d)
  
  
# Measuring the Fitness Score of each chromosome in the population
fitness_score = fitness_value/fitness_value.sum()*100
fs = np.round(fitness_score, 3)
Y = fs.reshape(-1, 1)
print("Fitness Score:\n", Y)


# Merge New Population with Fitness Score. And sort the merged array basis on best fitness score
Z = [[x, y] for x, y in zip(X, Y)]
sorted_Z = sorted(Z, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z in sorted_Z:
    print(z)
    

# Multipoint Crossover
def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[6.69,  4.35, 53  , 18.28], [17.75,  7.68, 38  ,  1.72], [19.56, 13.41, 51  , 17.98], [10.82,  8.37, 52  , 22.45]]
num_offsprings = 35
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen1: Child: \n", c1)

# Find out the Fitness Value of Children
Z1 = []
for i in range(35):
    Z1.append(100 - (((c1[i][0] - c1[i][1]) * (100 - c1[i][2])) / c1[i][3]))

array = np.array(Z1)
new_array = array.reshape(35, 1)

# Find out the Fitness Score of Children of Generation 1 
def SumofArray(arr):
    sum=0
    n = len(arr)
    for Z1 in range(n):
        sum = sum + arr[Z1]
    return sum

ff1 = ((Z1/SumofArray(Z1))*100)
fs1 = np.array(ff1)
Y1 = np.round(fs1, 3)
y1 = Y1.reshape(35, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)

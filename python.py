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
    

# Multipoint Crossover for 1st Generation-

def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[ 12.73,  16.66,   0.76,  58.69, 464.  , 152.  , 213.  ,   0.76,
         0.62], [ 19.05,  11.89,   1.17,  85.66, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [  7.61,  14.09,   0.88,  69.42, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 17.47,  24.14,   0.52,  80.7 , 453.  , 119.  , 137.  ,   0.66,
         0.61], [  8.59,  11.39,   0.64,  73.54, 471.  ,  86.  , 191.  ,   0.46,
         0.39], [ 16.09,  11.63,   0.78,  59.78, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 15.38,   3.18,   0.7 ,  72.97, 461.  ,  70.  , 194.  ,   0.57,
         1.23], [ 18.09,   7.77,   0.66,  72.22, 483.  , 139.  ,  44.  ,   0.52,
         1.21], [ 10.34,   7.46,   0.72,  77.79, 453.  ,  38.  , 242.  ,   0.16,
         0.33], [ 16.62,  13.64,   0.87,  81.75, 416.  , 103.  , 175.  ,   1.84,
         0.35], [ 18.47,  24.81,   1.17,  73.57, 403.  , 113.  , 169.  ,   0.62,
         0.72], [ 15.02,  21.09,   0.96,  65.5 , 480.  ,  78.  , 125.  ,   0.78,
         0.57], [ 15.84,   5.98,   1.08,  54.08, 462.  , 121.  , 105.  ,   1.44,
         0.57], [  6.4 ,  10.13,   0.54,  59.24, 387.  , 129.  , 202.  ,   0.56,
         0.08], [  7.67,   7.03,   0.67,  84.59, 443.  , 150.  ,  53.  ,   1.17,
         0.44], [ 18.3 ,  17.2 ,   0.5 ,  80.64, 400.  ,  68.  , 204.  ,   1.13,
         0.71], [ 16.21,  12.57,   0.44,  51.89, 481.  ,  26.  , 178.  ,   0.65,
         0.84], [  8.06,   3.33,   0.96,  81.52, 431.  ,  99.  , 137.  ,   0.17,
         0.94], [  6.24,  15.06,   0.59,  56.03, 485.  ,  94.  ,  75.  ,   0.99,
         1.34], [  6.89,  19.71,   0.88,  50.32, 394.  , 146.  , 131.  ,   0.73,
         0.3 ], [ 18.81,  18.37,   0.68,  59.9 , 381.  , 149.  , 114.  ,   0.55,
         1.07], [ 11.31,  19.74,   0.62,  70.13, 377.  , 112.  , 178.  ,   0.42,
         1.1], [ 14.85,   5.12,   0.76,  74.87, 415.  , 112.  , 121.  ,   0.72,
         1.49], [ 15.61,  21.19,   1.01,  75.49, 435.  , 105.  ,  69.  ,   0.42,
         0.34], [ 12.51,  25.66,   0.69,  76.69, 477.  ,  40.  , 103.  ,   0.18,
         0.17], [ 16.28,   3.4 ,   0.86,  54.21, 473.  ,  46.  , 130.  ,   1.2 ,
         0.51], [ 11.79,   8.83,   1.07,  50.86, 313.  , 130.  , 244.  ,   0.54,
         0.73], [ 12.19,   6.33,   0.88,  77.72, 352.  , 148.  , 126.  ,   0.18,
         1.11], [  7.  ,  10.33,   0.68,  71.86, 456.  ,  53.  , 123.  ,   1.34,
         0.3 ], [  6.66,   6.89,   0.71,  67.71, 403.  ,  23.  , 239.  ,   1.95,
         0.19]]
num_offsprings = 80
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen1: Child: \n", c1)


# Find out the Fitness Value of Children
Z1 = []
for i in range(80):
    Z1.append((0.2 * c1[i][0]) + (0.1 * c1[i][1]) + (0.1 * c1[i][2]) + (0.1 * c1[i][3]) + (0.15 * c1[i][4]) + (0.15 * c1[i][5]) + (0.1 * c1[i][6]) + (0.05 * c1[i][7]) + (0.05 * c1[i][8]))

array = np.array(Z1)
new_array = array.reshape(80, 1)

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
y1 = Y1.reshape(80, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)
    
    
    
 # Multipoint Crossover for 2nd Generation-

import numpy as np
import random
def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[ 16.28,   3.4 ,   0.86,  54.21, 464.  , 152.  , 213.  ,   0.76,
         0.62], [ 15.61,  21.19,   1.01,  75.49, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 16.62,  13.64,   0.87,  81.75, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.09,   7.77,   0.66,  72.22, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.81,  18.37,   0.68,  59.9 , 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 15.61,  21.19,   1.01,  75.49, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.62,  13.64,   0.87,  81.75, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.21,  12.57,   0.44,  51.89, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 12.19,   6.33,   0.88,  77.72, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.21,  12.57,   0.44,  51.89, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.62,  13.64,   0.87,  81.75, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 11.79,   8.83,   1.07,  50.86, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.09,  11.63,   0.78,  59.78, 471.  ,  86.  , 191.  ,   0.46,
         0.39], [  7.67,   7.03,   0.67,  84.59, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 15.61,  21.19,   1.01,  75.49, 453.  , 119.  , 137.  ,   0.66,
         0.61], [ 17.47,  24.14,   0.52,  80.7 , 453.  ,  38.  , 242.  ,   0.16,
         0.33], [ 16.28,   3.4 ,   0.86,  54.21, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 18.81,  18.37,   0.68,  59.9 , 453.  , 119.  , 137.  ,   0.66,
         0.61], [  6.4 ,  10.13,   0.54,  59.24, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 12.19,   6.33,   0.88,  77.72, 453.  , 119.  , 137.  ,   0.66,
         0.61], [ 15.38,   3.18,   0.7 ,  72.97, 453.  , 119.  , 137.  ,   0.66,
         0.61], [ 16.09,  11.63,   0.78,  59.78, 453.  , 119.  , 137.  ,   0.66,
         0.61], [ 18.81,  18.37,   0.68,  59.9 , 453.  ,  38.  , 242.  ,   0.16,
         0.33], [ 18.81,  18.37,   0.68,  59.9 , 387.  , 129.  , 202.  ,   0.56,
         0.08], [ 18.09,   7.77,   0.66,  72.22, 387.  , 129.  , 202.  ,   0.56,
         0.08]]
num_offsprings = 60
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen2: Child: \n", c1)


# Find out the Fitness Value of Children
Z1 = []
for i in range(60):
    Z1.append((0.2 * c1[i][0]) + (0.1 * c1[i][1]) + (0.1 * c1[i][2]) + (0.1 * c1[i][3]) + (0.15 * c1[i][4]) + (0.15 * c1[i][5]) + (0.1 * c1[i][6]) + (0.05 * c1[i][7]) + (0.05 * c1[i][8]))

array = np.array(Z1)
new_array = array.reshape(60, 1)

# Find out the Fitness Score of Children of Generation 2
def SumofArray(arr):
    sum=0
    n = len(arr)
    for Z1 in range(n):
        sum = sum + arr[Z1]
    return sum

ff1 = ((Z1/SumofArray(Z1))*100)
fs1 = np.array(ff1)
Y1 = np.round(fs1, 3)
y1 = Y1.reshape(60, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)
    
    
  
 # Multipoint Crossover for 3rd Generation-
    
    def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[ 16.62,  13.64,   0.87,  81.75, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.09,   7.77,   0.66,  72.22, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.81,  18.37,   0.68,  59.9 , 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 15.61,  21.19,   1.01,  75.49, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.09,  11.63,   0.78,  59.78, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.09,   7.77,   0.66,  72.22, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 18.81,  18.37,   0.68,  59.9 , 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.21,  12.57,   0.44,  51.89, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [  7.67,   7.03,   0.67,  84.59, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 15.38,   3.18,   0.7 ,  72.97, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.09,  11.63,   0.78,  59.78, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 15.61,  21.19,   1.01,  75.49, 471.  ,  86.  , 191.  ,   0.46,
         0.39], [ 16.28,   3.4 ,   0.86,  54.21, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.62,  13.64,   0.87,  81.75, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 15.61,  21.19,   1.01,  75.49, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 11.79,   8.83,   1.07,  50.86, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.09,  11.63,   0.78,  59.78, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 15.61,  21.19,   1.01,  75.49, 453.  , 119.  , 137.  ,   0.66,
         0.61], [ 16.21,  12.57,   0.44,  51.89, 451.  , 108.  , 183.  ,   1.37,
         1.19], [ 18.09,   7.77,   0.66,  72.22, 453.  , 119.  , 137.  ,   0.66,
         0.61]]
num_offsprings = 40
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen3: Child: \n", c1)


# Find out the Fitness Value of Children
Z1 = []
for i in range(40):
    Z1.append((0.2 * c1[i][0]) + (0.1 * c1[i][1]) + (0.1 * c1[i][2]) + (0.1 * c1[i][3]) + (0.15 * c1[i][4]) + (0.15 * c1[i][5]) + (0.1 * c1[i][6]) + (0.05 * c1[i][7]) + (0.05 * c1[i][8]))

array = np.array(Z1)
new_array = array.reshape(40, 1)

# Find out the Fitness Score of Children of Generation 3
def SumofArray(arr):
    sum=0
    n = len(arr)
    for Z1 in range(n):
        sum = sum + arr[Z1]
    return sum

ff1 = ((Z1/SumofArray(Z1))*100)
fs1 = np.array(ff1)
Y1 = np.round(fs1, 3)
y1 = Y1.reshape(40, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)
    
    
    
  
# Multipoint Crossover for 4th Generation-

def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[ 16.62,  13.64,   0.87,  81.75, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 15.61,  21.19,   1.01,  75.49, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.81,  18.37,   0.68,  59.9 , 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 16.62,  13.64,   0.87,  81.75, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 15.61,  21.19,   1.01,  75.49, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.09,  11.63,   0.78,  59.78, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.09,   7.77,   0.66,  72.22, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 18.81,  18.37,   0.68,  59.9 , 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.21,  12.57,   0.44,  51.89, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [  7.67,   7.03,   0.67,  84.59, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.28,   3.4 ,   0.86,  54.21, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 16.09,  11.63,   0.78,  59.78, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.21,  12.57,   0.44,  51.89, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.62,  13.64,   0.87,  81.75, 471.  ,  86.  , 191.  ,   0.46,
         0.39], [ 15.61,  21.19,   1.01,  75.49, 471.  ,  86.  , 191.  ,   0.46,
         0.39]]
num_offsprings = 30
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen4: Child: \n", c1)


# Find out the Fitness Value of Children
Z1 = []
for i in range(30):
    Z1.append((0.2 * c1[i][0]) + (0.1 * c1[i][1]) + (0.1 * c1[i][2]) + (0.1 * c1[i][3]) + (0.15 * c1[i][4]) + (0.15 * c1[i][5]) + (0.1 * c1[i][6]) + (0.05 * c1[i][7]) + (0.05 * c1[i][8]))

array = np.array(Z1)
new_array = array.reshape(30, 1)

# Find out the Fitness Score of Children of Generation 4
def SumofArray(arr):
    sum=0
    n = len(arr)
    for Z1 in range(n):
        sum = sum + arr[Z1]
    return sum

ff1 = ((Z1/SumofArray(Z1))*100)
fs1 = np.array(ff1)
Y1 = np.round(fs1, 3)
y1 = Y1.reshape(30, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)

    
    
 # Multipoint Crossover for 5th Generation-

def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[ 16.62,  13.64,   0.87,  81.75, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 15.61,  21.19,   1.01,  75.49, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.81,  18.37,   0.68,  59.9 , 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.09,   7.77,   0.66,  72.22, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 16.62,  13.64,   0.87,  81.75, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 15.61,  21.19,   1.01,  75.49, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.09,  11.63,   0.78,  59.78, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.81,  18.37,   0.68,  59.9 , 486.  , 135.  , 129.  ,   1.59,
         1.33], [  7.67,   7.03,   0.67,  84.59, 486.  , 135.  , 129.  ,   1.59,
         1.33], [ 16.28,   3.4 ,   0.86,  54.21, 460.  , 153.  , 156.  ,   1.9 ,
         1.47]]
num_offsprings = 20
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen5: Child: \n", c1)


# Find out the Fitness Value of Children
Z1 = []
for i in range(20):
    Z1.append((0.2 * c1[i][0]) + (0.1 * c1[i][1]) + (0.1 * c1[i][2]) + (0.1 * c1[i][3]) + (0.15 * c1[i][4]) + (0.15 * c1[i][5]) + (0.1 * c1[i][6]) + (0.05 * c1[i][7]) + (0.05 * c1[i][8]))

array = np.array(Z1)
new_array = array.reshape(20, 1)

# Find out the Fitness Score of Children of Generation 5
def SumofArray(arr):
    sum=0
    n = len(arr)
    for Z1 in range(n):
        sum = sum + arr[Z1]
    return sum

ff1 = ((Z1/SumofArray(Z1))*100)
fs1 = np.array(ff1)
Y1 = np.round(fs1, 3)
y1 = Y1.reshape(20, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)
    
    
   
 # Multipoint Crossover for 6th Generation-
    
import numpy as np
import random
def crossover(parents, num_offsprings):
    offsprings = []
    for i in range(num_offsprings):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        offsprings.append(offspring)
    return offsprings

parents = [[ 16.62,  13.64,   0.87,  81.75, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 15.61,  21.19,   1.01,  75.49, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.09,   7.77,   0.66,  72.22, 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 18.81,  18.37,   0.68,  59.9 , 460.  , 153.  , 156.  ,   1.9 ,
         1.47], [ 16.62,  13.64,   0.87,  81.75, 486.  , 135.  , 129.  ,   1.59,
         1.33]]
num_offsprings = 10
offsprings = crossover(parents, num_offsprings)
child = np.array(offsprings)
c1 = child
print("Gen6: Child: \n", c1)


# Find out the Fitness Value of Children
Z1 = []
for i in range(10):
    Z1.append((0.2 * c1[i][0]) + (0.1 * c1[i][1]) + (0.1 * c1[i][2]) + (0.1 * c1[i][3]) + (0.15 * c1[i][4]) + (0.15 * c1[i][5]) + (0.1 * c1[i][6]) + (0.05 * c1[i][7]) + (0.05 * c1[i][8]))

array = np.array(Z1)
new_array = array.reshape(10, 1)

# Find out the Fitness Score of Children of Generation 6
def SumofArray(arr):
    sum=0
    n = len(arr)
    for Z1 in range(n):
        sum = sum + arr[Z1]
    return sum

ff1 = ((Z1/SumofArray(Z1))*100)
fs1 = np.array(ff1)
Y1 = np.round(fs1, 3)
y1 = Y1.reshape(10, 1)
print("Fitness Score:\n", y1)

# Sort the merged array basis on best fitness score
a1 = [[x, y] for x, y in zip(c1, y1)]
sorted_a1 = sorted(a1, key=lambda x: x[1], reverse=True)
print("\n After Sorted basis on Fitness Score:")
for z1 in sorted_a1:
    print(z1)
    
    
   
 # Multipoint Crossover for 7th Generation-
    
    

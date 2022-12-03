# Import Libraries
import numpy
import random
import pandas as pd
import ga


"""
The S=target is to maximize this equation ASAP:
    S=100-(((n-na)(100-h))/D)
    where (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)=(12.7,10.5,15.71,19.62,13.65,14.4,15.26,4.87,18.13,17.28,15.66)
    where (na1,na2,na3,na4,na5,na6,na7,na8,na9,na10,na11)=(12.46,10.23,15.10,15.6,3.9,11.9,11.2,3.8,11.8,9.5,8.4)
    where (h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11)=(60,60,30,35,30,30,40,40,30,30,30)
    where (D1,D2,D3,D4,D4,D5,D6,D7,D8,D9,D10,D11)=(300,300,1500,1000,600,960,240,2000,400,300,400)
    What are the best values for S?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""


# Inputs of the equation.
efficiency_inputs = [12.7,10.5,15.71,19.62,13.65,14.4,15.26,4.87,18.13,17.28,15.66]
efficiency_aged_inputs = [12.46,10.23,15.10,15.6,3.9,11.9,11.2,3.8,11.8,9.5,8.4]
humidity_inputs = [60,60,30,35,30,30,40,40,30,30,30]
duration_inputs =[300,300,1500,1000,600,960,240,2000,400,300,400]


# Number of the population we are looking to optimize.
num_population = 1
"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 20
num_parents_mating = 20
# Defining the population size.
pop_size = (sol_per_pop,num_population) #The population will have sol_per_pop chromosome where each chromosome has num_population genes.


# Creating the initial population.
new_population1 = numpy.random.uniform(low=4.0, high=19.62, size=pop_size)
df1 = pd.DataFrame(new_population1, columns=['efficiency_inputs'])
new_population2 = numpy.random.uniform(low=3.8, high=15.6, size=pop_size)

df2 = pd.DataFrame(new_population2, columns=['efficiency_aged_inputs'])
new_population3 = numpy.random.randint(low=30, high=60, size=pop_size)
     
df3 = pd.DataFrame(new_population3, columns=['humidity_inputs'])
new_population4 = numpy.random.randint(low=240, high=3000, size=pop_size)

df4 = pd.DataFrame(new_population4, columns=['duration_inputs'])
new_population = numpy.array([df1, df2, df3, df4])
print (new_population.transpose())
      

# Measuring the Fitness Value of each chromosome in the population.
for num in range(1):
      
      efficiency = new_population1
      efficiency_aged = new_population2
      humidity = new_population3
      duration = new_population4  
      
      Stability_index = pd.DataFrame(data= (100-(((efficiency-efficiency_aged)*(100-humidity))/duration)))
      fitness_function = np.round(Stability_index, 2)
      fitness_value = np.array(fitness_function)
      print("Fitness Value:\n", fitness_value)
      
      # Measuring the Fitness Score of each chromosome in the population.
      def SumofArray(arr):
    sum=0
    n = len(arr)
    for fitness_value in range(n):
        sum = sum + arr[fitness_value]
    return sum

ff = ((fitness_value/SumofArray(fitness_value))*100)
fitness_score = np.array(ff)
print("Fitness Score:\n", fitness_score)

# Multipoint Crossover
def single_point_crossover(Parent1, Parent2, x) :
    Parent1_new = np.append(Parent1[:x], Parent2[x:])
    Parent2_new = np.append(Parent2[:x], Parent1[x:])
    return Parent1_new, Parent2_new

def multi_point_crossover(Parent1, Parent2, X):
    for i in X:
        Parent1, Parent2 = single_point_crossover(Parent1, Parent2, i)
    return Parent1, Parent2
   
Parent1 = np.array([12.7, 12.46, 60, 300])
Parent2 = np.array([15.71, 15.1, 30, 1500])
a=0;
i=0
while i<4:
    j=0
    while j<4:
        X = np.array([i,j])
        Child1=multi_point_crossover(Parent1, Parent2, X)
        a=a+1
        print("Generation",a, "=",  Child1)
        print("\n")
        j=j+1
    i=i+1

#script in Python 3.7
import numpy as np
import matplotlib.pyplot as plt
import math

# S = susceptible individuals
# I = infectious individuals
# β = infectious rate, controls the rate of spread which represents the probability of transmitting disease between a susceptible and an infectious individual
# γ = recovery rate, is determined by the inverse of the average duration of infection
# N = S + I totall population (constant)
# R = β / γ basic reproduction number

#N = int(input("Enter totall population:"))
#print("Totall population :" + N)
N = 1000
population_S = []
population_S += [N]
population_I = []
population_I += [0]
beta = np.random.rand()
gamma = np.random.rand()
print(beta / gamma)

for time in range(0,1000):
    delta_12 = 0 #from Susceptible to Infectious
    delta_21 = 0 #from Infectious to Susceptible
    R = beta / gamma
    #print(beta)
    if R > 1:
        print("Need of an intervention (R>1)")
        #β must dicrise
        beta = math.exp(-time)
    R = beta / gamma
    if 0.87 < R < 0.97:
        print("The intervention was effective")

    prob_of_infection = beta*population_S[-1]/N
    #Susceptible
    for atoms in range(0,population_S[-1]):
        if(np.random.rand() < prob_of_infection):
            delta_12 += 1

    prob_of_recovery = gamma
    #Infectious
    for atoms in range(0,population_I[-1]):
        if(np.random.rand() < prob_of_recovery):
            delta_21 += 1
    #calculating new populations
    N_1 = delta_21 - delta_12
    N_2 = delta_12 - delta_21
    #adding the populations to their populations
    population_S += [population_S[-1] + N_1]
    population_I += [population_I[-1] + N_2]

plt.figure(figsize=(16,9))
plt.rc('font', size=22)
plt.xlabel('Time')
plt.ylabel('Population I, S')

plt.plot(population_S, color='green', linestyle='-', linewidth=4)
plt.plot(population_I, color='red', linestyle='-', linewidth=4)
plt.show()

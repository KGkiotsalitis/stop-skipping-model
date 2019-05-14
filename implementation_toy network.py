#Description: This code sets-up the stop-skipping model and the model that evaluates its objective function
#Author: Dr. K.Gkiotsalitis
#Date: 08 May 2019
#License: MIT

import numpy as np
import math
import itertools
import time
from stop_skipping_model import w,w_downstream_estimate, tilde_w,l_lambda,l,m,u,x,b,v,k,t,a,d,h,f

limit_N=4
limit_S=5
r1=4 #seconds
r2=2 #seconds
delta=20 #seconds
c1=10 #dollars/h
c2=5 #dollars/h
c3=7 #dollars/h
tilde_input_d=np.zeros(limit_N)
expected_headway=600 #sec

for i in range(0,len(tilde_input_d)):
    tilde_input_d[i]=600*i

t_w_input=np.zeros((limit_S,limit_S))
travel_times=60*np.ones((limit_N,limit_S-1))
l_lambda_input=np.zeros((limit_S,limit_S))
for i in range(0,limit_S):
    for j in range(0,limit_S):
        if j>i:
            l_lambda_input[i][j]=0.05
            t_w_input[i][j]=12
        else:
            l_lambda_input[i][j]=0
            t_w_input[i][j] = 0

#Initialize the decision variable
the_x=np.ones((limit_N,limit_S))
for n in range(0,limit_N):
    the_x[n][0]=1
    the_x[n][limit_S-1]=1

Time=time.time()
print(f(the_x,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
print('computational time in sec',time.time()-Time)

'''
########
# Brute Force Approach
Time=time.time()

The_L=itertools.product(range(2),repeat=limit_N*limit_S)
counter=0; optimal_solution=+np.infty

for each in The_L:
    counter=-1; feasibility='yes'
    for n in range(0,limit_N):
        for s in range(0,limit_S):
            counter=counter+1
            the_x[n][s]=float(each[counter])
    for n in range(0, limit_N):
        if the_x[n][0] == 0.0 or the_x[n][limit_S - 1] == 0.0:
            feasibility = 'no'
        for s in range(0, limit_S):
            if n>1 and the_x[n][s]+the_x[n-1][s]<1.0:
                    feasibility='no'

    if feasibility=='yes':
        of_value=f(the_x,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
        if optimal_solution>of_value:
            optimal_solution=of_value
            solution=np.copy(the_x)

print(optimal_solution)
print(solution)
########
print('computational time in sec',time.time()-Time)
'''

'''
########
# Sequential Hill Climbing Approach
Time=time.time()
the_x=np.ones((limit_N,limit_S))

mu_max=4; count=0; count_0=0; N_set=[];S_set=[]
while count<mu_max:
    count=count+1
    performance=f(the_x,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    n_prime=np.random.choice(np.arange(0,limit_N));s_prime=np.random.choice(np.arange(1,limit_S-1))

    del N_set[:]; N_set=[]
    N_set.append(n_prime)
    for i in range(0,limit_N):
        if i!=n_prime:
            N_set.append(i)
    del S_set[:]; S_set=[]
    S_set.append(s_prime)
    for i in range(1,limit_S-1):
        if i!=s_prime:
            S_set.append(i)
    #print(N_set,S_set)

    for n in range(0,limit_N):
        #n=np.random.choice(np.arange(0,limit_N))
        for s in S_set:#range(1,limit_S-1):
            #s = np.random.choice(np.arange(1, limit_S-1))
            for eta in [0, 1]:
                count_0 = count_0 + 1
                print(count_0,performance)
                performance=f(the_x,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
                hold_value=the_x[n][s]
                the_x[n][s]=eta
                #Check Solution Feasibility
                if n!=0 and n!=limit_N-1 and (the_x[n][s]+the_x[n-1][s]<1 or the_x[n+1][s]+the_x[n][s]<1):
                    the_x[n][s]=hold_value
                if n==0 and the_x[n+1][s]+the_x[n][s]<1:
                    the_x[n][s]=hold_value
                if n==limit_N-1 and the_x[n][s]+the_x[n-1][s]<1:
                    the_x[n][s]=hold_value
                ####
                if the_x[n][s]!=hold_value:
                    if f(the_x,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)>=performance: the_x[n][s]=hold_value
    #print(the_x,f(the_x))
print(the_x)
print('computational time in sec',time.time()-Time)
'''

'''
########
# Genetic Algorithm Approach
Time=time.time()
max_gen=4 #population generations - a hyperparameter
population_size=52 #population size - a hyperparameter
p_c=0.4 #mutation rate - a hyperparameter
half_pop_size=int(population_size*0.5)
pop_solution = np.ones((population_size,limit_N,limit_S))
for i in range(0,population_size):
    for n in range(0,limit_N):
        for s in range(0,limit_S):
            if s==0 or s==limit_S-1:
                pop_solution[i][n][s]=1
            else:
                pop_solution[i][n][s]=np.random.choice([0,1])
            if n>0:
                if pop_solution[i][n-1][s]+pop_solution[i][n][s]<1: pop_solution[i][n][s]=1

#print (pop_solution)
fitness=[]
for i in range(0,population_size):
    for n in range(0,limit_N):
        for s in range(0,limit_S):
            the_x[n][s]=pop_solution[i][n][s]
    fitness.append(f(the_x,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
print(fitness)
print('incumbent_solution,',min(fitness))
reproduction_members = sorted(range(len(fitness)), key=lambda k: fitness[k])
print(reproduction_members)

for generations in range(1,max_gen+1):
    #Crossover
    for i in range(0,half_pop_size):
        crossover_point_n=np.random.choice(np.arange(1,limit_N-1))
        #crossover_point_s=np.random.choice(1,limit_S-1)
        for n in range(0,limit_N):
            for s in range(0,limit_S):
                if n<=crossover_point_n:
                    if s==0 or s==limit_S-1:
                        pop_solution[half_pop_size-1+i][n][s]=1
                    else:
                        pop_solution[half_pop_size-1+i][n][s]=pop_solution[reproduction_members[i]][n][s]
                    if n>0 and pop_solution[half_pop_size+i][n-1][s]+pop_solution[half_pop_size+i][n][s]<1: pop_solution[half_pop_size+i][n][s]=1
                if n>crossover_point_n:
                    if s==0 or s==limit_S-1:
                        pop_solution[half_pop_size-1+i][n][s]=1
                    else:
                        pop_solution[half_pop_size-1+i][n][s]=pop_solution[reproduction_members[half_pop_size-1+i+1]][n][s]
                    if n>0 and pop_solution[half_pop_size-1+i][n-1][s]+pop_solution[half_pop_size-1+i][n][s]<1: pop_solution[half_pop_size-1+i][n][s]=1
    # Mutation
    for i in range(0, population_size):
        for n in range(0, limit_N):
            for s in range(0, limit_S):
                if s == 0 or s == limit_S - 1:
                    pop_solution[i][n][s] = 1
                if s>0 and s<limit_S-1 and np.random.choice(np.arange(0,1.1,0.1))<p_c: #mutation step
                    if pop_solution[i][n][s]==1:
                        pop_solution[i][n][s]=0
                    else:
                        pop_solution[i][n][s] = 1
                if n > 0:
                    if pop_solution[i][n - 1][s] + pop_solution[i][n][s] < 1: pop_solution[i][n][s] = 1

    del fitness[:]; fitness = []
    for i in range(0, population_size):
        for n in range(0, limit_N):
            for s in range(0, limit_S):
                the_x[n][s] = pop_solution[i][n][s]
        fitness.append(f(the_x, limit_N, limit_S, r1, r2, delta, c1, c2, c3, tilde_input_d, expected_headway, t_w_input,
                         travel_times, l_lambda_input))
    print(fitness)
    print('incumbent_solution,', min(fitness))
    reproduction_members=sorted(range(len(fitness)), key=lambda k: fitness[k])
    print(reproduction_members)

print ('GA_solution',pop_solution[reproduction_members[0]][:][:])
print('GA_solution_performance,',min(fitness))
print('computational time in sec',time.time()-Time)
'''
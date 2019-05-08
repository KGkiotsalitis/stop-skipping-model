#Description: This code sets-up the stop-skipping model and the model that evaluates its objective function
#Author: Dr. K.Gkiotsalitis
#Date: 08 May 2019

import numpy as np
import math
import itertools
import  time

limit_N=4
limit_S=6
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
travel_times=60*np.ones((limit_N,limit_S))
l_lambda_input=np.zeros((limit_S,limit_S))
for i in range(0,limit_S):
    for j in range(0,limit_S):
        if j>i:
            l_lambda_input[i][j]=0.05
            t_w_input[i][j]=12
        else:
            l_lambda_input[i][j]=0
            t_w_input[i][j] = 0

def tilde_w(s,y):
    return(t_w_input[s-1][y-1])

def w(n,s,y,dec_var):
    value=0
    if n==1: #boundary condition
        value=tilde_w(s,y)
    if n>1:
        value=l(n-1,s,y,dec_var)+l_lambda(s,y)*h(n,s,dec_var)
    return (value)

def w_downstream_estimate(n,s,y,dec_var):
    value=0
    if n==1: #boundary condition
        value=tilde_w(s,y)
    if n>1:
        value=l(n-1,s,y,dec_var)+l_lambda(s,y)*expected_headway
    return (value)

def l_lambda(s,y):
    return l_lambda_input[s-1][y-1]

#function that returns the number of passengers destined to stop y who are stranded by bus n-1 at stop s
def l(n,s,y,dec_var):
    value=0
    if y<=s:
        value=0
    if y>s:
        value=w(n,s,y,dec_var)-w(n,s,y,dec_var)*x(n,s,dec_var)*x(n,y,dec_var)
    return (value)

def m(n,s,dec_var):
    value=0
    for y in range(s+1,limit_S+1):
        value=value+l(n,s,y,dec_var)
    return (value)

def u(n,s,dec_var):
    value=0
    if s==limit_S:
        value=0
    if s<limit_S:
        for y in range(s+1,limit_S+1):
            value=value+w_downstream_estimate(n,s,y,dec_var)*x(n,y,dec_var)
        value=x(n,s,dec_var)*value
    return(value)

def x(n,s,dec_var):
    return(dec_var[n-1][s-1])

def b(n,s,y,dec_var):
    value=0
    if y<=s:
        value=0
    if y>s:
        value=x(n,y,dec_var)*w(n,s,y,dec_var)*x(n,y,dec_var)
    return(value)

def v(n,s,dec_var):
    if s==1:
        value=0
    if s>1:
        value=0
        for y in range(1,s-1+1):
            value=value+w(n,y,s,dec_var)*x(n,y,dec_var)
        value=value*x(n,s,dec_var)
    return(value)

def k(n,s,dec_var):
    return(r2*v(n,s,dec_var)+r1*u(n,s,dec_var))

def t(n,s):
    return travel_times[n-1][s-1]

def a(n,s,dec_var):
    value=0
    if s==2:
        value=tilde_d(n)+t(n,2)+(delta/2.0)*(x(n,1,dec_var)+x(n,2,dec_var))
    if s>2:
        value=d(n,s-1,dec_var)+t(n,s)+(delta/2.0)*(x(n,s-1,dec_var)+x(n,s,dec_var))
    return(value)

def d(n,s,dec_var):
    return(a(n,s,dec_var)+k(n,s,dec_var))

def tilde_d(n):
    return tilde_input_d[n-1]

def h(n,s,dec_var):
    value=0
    if s==1:
        value=tilde_d(n)-tilde_d(n-1)
        #print (value)
    if s>1:
        value=d(n,s,dec_var)-d(n-1,s,dec_var)
    return(value)



def f(dec_var):
    value=0; value1=0; value2=0; value3=0
    for n in range(3,limit_N+1):
        for s in range(1,limit_S+1):
            value1=value1+(u(n,s,dec_var)-m(n-1,s,dec_var))*0.5*h(n,s,dec_var)+m(n-1,s,dec_var)*(0.5*h(n-1,s,dec_var)+h(n,s,dec_var))
    value=value*c1
    for n in range(3,limit_N+1):
        for s in range(1,limit_S):
            for y in range(s+1,limit_S+1):
                value2_prime=0
                for z in range(s+1,y+1):
                    value2_prime=value2_prime+(t(n,z)+(k(n,z,dec_var)+delta)*x(n,z,dec_var))
                value2=value2+value2_prime*b(n,s,y,dec_var)
    value=value+c2*value2
    for n in range(3,limit_N+1):
        for s in range(2,limit_S+1):
            value3=value3+(t(n,s)+(k(n,s,dec_var)+delta)*x(n,s,dec_var))
    value=value+c3*value3
    return(value)

#Initialize the decision variable
the_x=np.ones((limit_N,limit_S))
for n in range(0,limit_N):
    the_x[n][0]=1
    the_x[n][limit_S-1]=1

print(f(the_x))

#print (a(1,2,the_x),k(1,2,the_x),d(1,2,the_x))
#print (a(1,3,the_x),k(1,3,the_x),d(1,3,the_x))
#print (a(2,2,the_x),k(2,2,the_x),d(2,2,the_x),h(2,2,the_x))


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
        of_value=f(the_x)
        if optimal_solution>of_value:
            optimal_solution=of_value
            solution=np.copy(the_x)

print(optimal_solution)
print(solution)
########

print(time.time()-Time)

########
# Sequential Hill Climbing Approach
Time=time.time()
the_x=np.ones((limit_N,limit_S))
mu_max=1; count=0
while count<mu_max:
    count=count+1
    #n=np.random.choice(np.arange(0,limit_N))
    #s=np.random.choice(np.arange(1,limit_S-1))
    performance=f(the_x)
    #set=np.arange(1,limit_S-2)
    #new_set = np.delete(set, s-2)
    #print('information',s, set, new_set)

    for n in range(0,limit_N):
        for s in range(1,limit_S-1):
            for eta in [0, 1]:
                print(performance)
                performance=f(the_x)
                hold_value=the_x[n][s]
                the_x[n][s]=eta
                #Check Solution Feasibility
                if n!=0 and n!=limit_N-1 and (the_x[n][s]+the_x[n-1][s]<1 or the_x[n+1][s]+the_x[n][s]<1):
                    the_x[n][s]=hold_value
                if n==1 and the_x[n+1][s]+the_x[n][s]<1:
                    the_x[n][s]=hold_value
                if n==limit_N-1 and the_x[n][s]+the_x[n-1][s]<1:
                    the_x[n][s]=hold_value
                ####
                if the_x[n][s]!=hold_value:
                    if f(the_x)>=performance: the_x[n][s]=hold_value
    print(the_x,f(the_x))
print(time.time()-Time)


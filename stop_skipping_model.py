#Description: This code sets-up the stop-skipping model and the model that evaluates its objective function
#Author: Dr. K.Gkiotsalitis
#Date: 08 May 2019
#License: MIT

import numpy as np
import math
import itertools
import  time


def tilde_w(s,y,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return(t_w_input[s-1][y-1])

def w(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if n==1: #boundary condition
        value=tilde_w(s,y,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    if n>1:
        value=l(n-1,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
              +l_lambda(s,y,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*h(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    return (value)

def w_downstream_estimate(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if n==1: #boundary condition
        value=tilde_w(s,y,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    if n>1:
        value=l(n-1,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+l_lambda(s,y,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*expected_headway
    return (value)

def l_lambda(s,y,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return l_lambda_input[s-1][y-1]

#function that returns the number of passengers destined to stop y who are stranded by bus n-1 at stop s
def l(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if y<=s:
        value=0
    if y>s:
        value=w(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
              -w(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*x(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*x(n,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    return (value)

def m(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    for y in range(s+1,limit_S+1):
        value=value+l(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    return (value)

def u(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if s==limit_S:
        value=0
    if s<limit_S:
        for y in range(s+1,limit_S+1):
            value=value+w_downstream_estimate(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*x(n,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
        value=x(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*value
    return(value)

def x(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return(dec_var[n-1][s-1])

def b(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if y<=s:
        value=0
    if y>s:
        value=x(n,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*w(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*x(n,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    return(value)

def v(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    if s==1:
        value=0
    if s>1:
        value=0
        for y in range(1,s-1+1):
            value=value+w(n,y,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*x(n,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
        value=value*x(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    return(value)

def k(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return(r2*v(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+r1*u(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))

def t(n,s,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return travel_times[n-1][s-2]

def a(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if s==2:
        value=tilde_d(n,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+t(n,2,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
              +(delta/2.0)*(x(n,1,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+x(n,2,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
    if s>2:
        value=d(n,s-1,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+t(n,s,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
              +(delta/2.0)*(x(n,s-1,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+x(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
    return(value)

def d(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return(a(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+k(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))

def tilde_d(n,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    return tilde_input_d[n-1]

def h(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0
    if s==1:
        value=tilde_d(n,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)-tilde_d(n-1,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
        #print (value)
    if s>1:
        value=d(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)-d(n-1,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    return(value)


def f(dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input):
    value=0; value1=0; value2=0; value3=0
    for n in range(2,limit_N+1):
        for s in range(1,limit_S+1):
            value1=value1+(u(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)-\
                           m(n-1,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))*0.5*h(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
                   +m(n-1,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)*(0.5*h(n-1,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
                                                                                                                    +h(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
    value=value*c1
    for n in range(2,limit_N+1):
        for s in range(1,limit_S):
            for y in range(s+1,limit_S+1):
                value2_prime=0
                for z in range(s+1,y+1):
                    value2_prime=value2_prime+(t(n,z,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+\
                                               (k(n,z,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+delta)*x(n,z,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
                value2=value2+value2_prime*b(n,s,y,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)
    value=value+c2*value2
    for n in range(2,limit_N+1):
        for s in range(2,limit_S+1):
            value3=value3+(t(n,s,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)\
                           +(k(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input)+delta)*x(n,s,dec_var,limit_N,limit_S,r1,r2,delta,c1,c2,c3,tilde_input_d,expected_headway,t_w_input,travel_times,l_lambda_input))
    value=value+c3*value3
    return(value)



#Sophia Cofone, 12/11/21, finalproject CS5002, coin flip with bayes applied

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def likelihood(trials,heads):
    #creating an array that holds all the values from 0-1 in 0.01 increments (this is all the possible models)
    theta = np.arange(0,1,0.01)
    #likelihood: comb gives us the coefficient for the binomial eq. the rest of this is the binomial eq.
    p_p = comb(trials,heads)*(theta**heads)*(1-theta)**(trials-heads)
    #normalizing the data
    p_norm = p_p/sum(p_p)
    
    return theta,p_norm

#setting the probability (.5 for unbiased coin)
p = .8

#determing the number of flips
trial1 = 25
trial2 = 100
trial3 = 1000

#determining the number of heads. 
#The binomial function selects a random point on the binombial distribution to be the number of heads
#This is just to create some relaistc simulated data
x,y = likelihood(trial1,np.random.binomial(trial1,p))
x2,y2 = likelihood(trial2,np.random.binomial(trial2,p))
x3,y3 = likelihood(trial3,np.random.binomial(trial3,p))

#setting up the plot
fig,ax = plt.subplots()
plt.title("Likelihood")
ax.set_xlabel('θ')
ax.set_ylabel('P')

#plotting trial 1
ax.plot(x,y,label='{} flips'.format(trial1))
#plotting trial 2
ax.plot(x2,y2,label='{} flips'.format(trial2))
#plotting trial 3
ax.plot(x3,y3,label='{} flips'.format(trial3))
#showing the plot
ax.legend()
plt.show()
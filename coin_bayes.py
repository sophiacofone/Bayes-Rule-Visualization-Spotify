#Sophia Cofone, 12/11/21, finalproject CS5002, coin flip binomial distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def likelihood(trials,heads):
    #creating an array that holds all the values from 0-1 in 0.01 increments (this is all the possible models)
    theta = np.arange(0,1,0.01)
    #likelihood: comb gives us the coefficient for the binomial eq. the rest of this is the binomial eq.
    p_p = comb(trials,heads)*(theta**heads)*(1-theta)**(trials-heads)
    return theta,p_p

def gauss(prior_avg,prior_sig):
    #creating an array that holds all the values from 0-1 in 0.01 increments (this is all the possible models)
    theta = np.arange(0,1,0.01)
    #calculates probability for all values of theta (binomial)
    p_p = np.exp(-(theta-prior_avg)**2/(2*prior_sig**2))
    #normalizing this
    p_norm = p_p/sum(p_p)

    return theta,p_norm

def posterior_normprior(trials, heads, prior_avg, prior_sig):
    #creating an array that holds all the values from 0-1 in 0.01 increments (this is all the possible models)
    theta = np.arange(0,1,0.01)
    #binomial likelihood * gaussian prior 
    p_p = ((theta**heads)*(1-theta)**(trials-heads))*np.exp(-(theta-prior_avg)**2/(2*prior_sig**2))
    #normalizing this
    p_norm = p_p/sum(p_p)

    return theta,p_norm

def main():
    #setting the probability (.5 for unbiased coin)
    p = .8

    #determing the number of flips
    trial1 = 25
    trial2 = 100
    trial3 = 1000

    #setting our prior avg and prior sig
    prior_avg = .5
    prior_sig = .03

    #determining the values to be plotted
    #first is the prior
    xp1,yp1 = gauss(prior_avg,prior_sig)

    #then the trials
    #The binomial function selects a random point on the binombial distribution to be the number of heads
    #This is just to create some relaistc simulated data
    x,y = posterior_normprior(trial1,np.random.binomial(trial1,p),prior_avg,prior_sig)
    x2,y2 = posterior_normprior(trial2,np.random.binomial(trial2,p),prior_avg,prior_sig)
    x3,y3 = posterior_normprior(trial3,np.random.binomial(trial3,p),prior_avg,prior_sig)

    #setting up the plot
    fig,ax = plt.subplots()
    plt.title("Posterior")
    ax.set_xlabel('θ')
    ax.set_ylabel('P')

    #plotting prior
    ax.plot(xp1,yp1,label='prior')
    #plotting trial 1
    ax.plot(x,y,label='{} flips'.format(trial1))
    #plotting trial 2
    ax.plot(x2,y2,label='{} flips'.format(trial2))
    #plotting trial 3
    ax.plot(x3,y3,label='{} flips'.format(trial3))
    #showing the plot
    ax.legend()
    plt.show()

main()
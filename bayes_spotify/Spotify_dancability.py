#Sophia Cofone, 12.5.21-12.11.21, CS5002, file is intented to be an application of bayes' rule using spotify genre data for final cs5002 project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

file = 'spotify_genre_final1.xlsx'
#imports the spotify data file, change to the name to your file or change your file name to this
cols = ["Genre","danceability"]
#specifies which columns in the data file we care about for the dataframe (table)
df = pd.read_excel(file, index_col=None)
#reads the excel file into a dataframe
df2 = pd.DataFrame(df[cols])
#makes a new data frame with the columns we care about (this will be the data frame used going fwd)
df2['highdance'] = df2['danceability'] >= .7
#this adds a new column named "highdance" to the dataframe. It is a boolean value that contains "true" if the song has a dancability rating of .7 or higher
#note this is arbitrary, I just selected .5 becuase it was about half the songs (half the songs were either higher or lower than .7)


def gauss(prior_avg,prior_sig):
    '''Function: The function gauss calculates the prior...the average danceability of genre
    Parameters: float
    Return: array'''
    #creating an array that holds all the values from 0-1 in 0.01 increments (this is all the possible models)
    theta = np.arange(0,1,0.01)
    #calculates probability for all values of theta (binomial eq)
    p_p = np.exp(-(theta-prior_avg)**2/(2*prior_sig**2))
    #normalizing
    p_norm = p_p/sum(p_p)

    return theta,p_norm

def likelihood(genre,df):
    '''Function: The function likelihood calculates P(D|M) using a binomial dist.
    Parameters: genre(str), a dataframe (df2)
    Return: array'''
    theta = np.arange(0,1,0.01)
    df_songs_dance = df[df.danceability >=0.7]
    sg = sum(df.Genre == genre)                   # number of songs that are genre (ex. 'rock')
    sgd = sum(df_songs_dance.Genre == genre)      # number of songs that are genre (ex. 'rock') and dancible
    #likelihood: comb gives us the coefficient for the binomial eq. the rest of this is the binomial eq.
    p_p = comb(sg,sgd)*(theta**sgd)*(1-theta)**(sg-sgd)
    #normalizing
    p_norm = p_p/sum(p_p)

    return theta,p_norm

def posterior_normprior(genre, df, prior_avg, prior_sig):
    '''Function: The function posterior calculates P(M|D)
    Parameters: genre(str), a dataframe (df2), float
    Return: array'''
    #creating an array that holds all the values from 0-1 in 0.01 increments (this is all the possible models)
    theta = np.arange(0,1,0.01)
    df_songs_dance = df[df.danceability >=0.7]
    sg = sum(df.Genre == genre)                   # number of songs that are genre (ex. 'rock')
    sgd = sum(df_songs_dance.Genre == genre)      # number of songs that are genre (ex. 'rock') and dancible
    #binomial likelihood * gaussian prior 
    p_p = comb(sg,sgd)*(theta**sgd)*(1-theta)**(sg-sgd)*(np.exp(-(theta-prior_avg)**2/(2*prior_sig**2)))
    #normalizing
    p_norm = p_p/sum(p_p)

    return theta,p_norm

def plot_genre(g):
    #dictonary containing our prior info
    priors = {'edm':(0.8,0.1),'hiphop':(0.6,0.1),'latin':(0.9,0.1),'pop':(0.2,0.1),'r&b':(0.5,0.1),'rap':(0.5,0.1),'rock':(0.4,0.1)}

    #determining the values to be plotted
    xp,yp = gauss(priors[g][0],priors[g][1])
    xl,yl = likelihood(g,df2)
    x,y = posterior_normprior(g,df2,priors[g][0],priors[g][1])

    #setting up the plot
    fig,ax = plt.subplots()
    plt.title(g)
    ax.set_xlabel('θ')
    ax.set_ylabel('P')

    #plotting prior
    ax.plot(xp,yp,label='prior')
    #plotting likelihood
    ax.plot(xl,yl,label='likelihood')  
    #plotting posterior
    ax.plot(x,y,label='posterior')

    #showing the plot
    ax.legend()
    plt.show()

def plot_posteriors():
    #dictonary containing our prior info
    priors = {'edm':(0.8,0.1),'hiphop':(0.6,0.1),'latin':(0.9,0.1),'pop':(0.2,0.1),'r&b':(0.5,0.1),'rap':(0.5,0.1),'rock':(0.4,0.1)}

    #determining the values to be plotted
    x,y = posterior_normprior('edm',df2,priors['edm'][0],priors['edm'][1])
    x1,y1 = posterior_normprior('hiphop',df2,priors['hiphop'][0],priors['hiphop'][1])
    x2,y2 = posterior_normprior('latin',df2,priors['latin'][0],priors['latin'][1])
    x3,y3 = posterior_normprior('pop',df2,priors['pop'][0],priors['pop'][1])
    x4,y4 = posterior_normprior('r&b',df2,priors['r&b'][0],priors['r&b'][1])
    x5,y5 = posterior_normprior('rap',df2,priors['rap'][0],priors['rap'][1])
    x6,y6 = posterior_normprior('rock',df2,priors['rock'][0],priors['rock'][1])

    #setting up the plot
    fig,ax = plt.subplots()
    plt.title('All Genres Posterior')
    ax.set_xlabel('θ')
    ax.set_ylabel('P')
  
    #plotting all genres
    ax.plot(x,y,label='edm')
    ax.plot(x1,y1,label='hiphop')
    ax.plot(x2,y2,label='latin')
    ax.plot(x3,y3,label='pop')
    ax.plot(x4,y4,label='r&b')
    ax.plot(x5,y5,label='rap')
    ax.plot(x6,y6,label='rock')

    #showing the plot
    ax.legend()
    plt.show()

def main():
    plot_genre(str(input("Please enter a Spotify music genre from this list: rock, edm, pop, hiphop, latin, r&b, rap: ")))
    plot_posteriors()
main()


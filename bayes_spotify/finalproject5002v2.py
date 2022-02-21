#Sophia Cofone, 12.5.21, CS5002, file is intented to be an application of bayes' rule using spotify genre data for final cs5002 project

import pandas as pd

file = 'spotify_genre_final.xlsx'
#imports the spotify data file, change to the name to your file or change your file name to this
cols = ["Genre","danceability"]
#specifies which columns in the data file we care about for the dataframe (table)
df = pd.read_excel(file, index_col=None)
#reads the excel file into a dataframe
df2 = pd.DataFrame(df[cols])
#makes a new data frame with the columns we care about (this will be the data frame used going fwd)
df2['highdance'] = df2['danceability'] >= .7
#this adds a new column named "highdance" to the dataframe. It is a boolean value that contains "true" if the song has a dancability rating of .7 or higher
#note this is arbitrary, I just selected .7 becuase it was about half the songs (half the songs were either higher or lower than .7)

def prior(df):
    '''Function: The function prior calculates P(A)...the probability of a particular song having a danceability rating 0.7 or above (total library of songs) 
    Parameters: a dataframe (df2)
    Return: float, P(A)'''
    numsongs = df.shape[0]
    num_dancable_songs = sum(df['highdance'])
    p_a = num_dancable_songs/numsongs

    return p_a

def likelihood(genre,df):
    '''Function: The function likelihood calculates P(B|A)...the probability of a song being in x (EDM, pop, etc.) genre given that it has a danceability rating 0.7 or higher
    Parameters: genre(str), a dataframe (df2)
    Return: float, P(B|A)'''
    df_songs_dance = df[df.danceability >=0.7]
    a = sum(df_songs_dance.Genre == genre)      # number of songs that are genre (ex. 'rock') and dancible
    y = sum(df['highdance'])                    # number of danceable songs
    p_b_a = a/y
    
    return p_b_a

def evidence(genre,df):
    '''Function: The function evidence calculates P(B)...the probability of a song being in x (EDM, pop, etc.) genre
    Parameters: genre(str), a dataframe (df2)
    Return: float, P(B)'''
    numsongs = df.shape[0]
    num_genre_songs = sum(df['Genre'] == genre)
    p_b = num_genre_songs/numsongs

    return p_b

def bayes(genre,df):
    '''Function: The function bayes (posterior) calculates P(A|B)...the probability of a particular song having a danceability rating 0.7 or above given the fact that it is in the x (EDM, pop, etc.) genre.
    Parameters: genre(str), a dataframe (df2)
    Return: float, P(A|B)'''
    p_a_b = ((likelihood(genre,df)) * (prior(df))) / (evidence(genre,df))
    
    return p_a_b

def main(): 
    print("Probability of any song in your Spotify library being highly dancable",(round((prior(df2))*100,0)),"%")
    genre = str(input("Please enter a Spotify music genre from this list: rock, edm, pop, hiphop, latin, r&b, rap: "))
    print("Probability of any song in your Spotify library being highly dancable GIVEN the genre is",genre,(round((bayes(genre,df2))*100,0)),"%")

main()


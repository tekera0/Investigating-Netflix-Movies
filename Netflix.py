# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

print(netflix_df)
#print(netflix_df[np.logical_and(netflix_df['release_year']>=1990,netflix_df['release_year']<2000)])

'''What was the most frequent movie duration in the 1990s? 
Save an approximate answer as an integer called duration (use 1990 as the decade's start year).'''

net = netflix_df[np.logical_and(netflix_df['release_year']>=1990,netflix_df['release_year']<2000)]

duration = net['duration'].mode()[0]
print(duration)

'''A movie is considered short if it is less than 90 minutes. 
Count the number of short action movies released in the 1990s and save this integer as short_movie_count.'''

short = net[np.array(net['duration']<90)]
#print(short['duration'])
short_movie_count = len(short[np.array(short['genre']== 'Action')])
print(short_movie_count)




plt.figure(figsize=(10, 6))

# Grouping by a categorical column like 'type' (e.g., Movie vs TV Show)
sns.scatterplot(
    data=netflix_df, 
    x='release_year', 
    y='duration', 
    hue='type', 
    palette='Set1',
    style='type'
)

plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.grid(True)
plt.show()
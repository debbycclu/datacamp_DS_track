import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')

#What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
select_movies = (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)
duration_movies = netflix_df[select_movies]['duration']
duration = int(duration_movies.mode()[0])

print(duration)


#A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.
action_movies_1990s = netflix_df[select_movies & netflix_df['genre'].str.contains('Action')]
short_movie_count = len(action_movies_1990s[action_movies_1990s['duration'] < 90])

print(short_movie_count)



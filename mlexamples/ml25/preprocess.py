import pandas as pd

movies = pd.read_csv('data/movie.csv')
ratings = pd.read_csv('data/rating.csv')
full_data = ratings.merge(movies, how='left', on='movieId')
full_data.to_csv('data/clean_ratings.csv')
<p style="text-align: center;">

# Dataset Description

The dataset `movies_and_shows.csv` contains information about various movies and shows.

import pandas as pd
df = pd.read_csv('/datasets/movies_and_shows.csv')

## Task 1: Data Cleaning

Let's clean the data to fix issues with the column names

df.info()
df = df.rename(
    columns = {
        '   name' : 'name',
    'Character' : 'character',
    'r0le' : 'role',
    'TITLE' : 'title',
    '  Type' : 'type',
    'release Year' : 'release_year',
    'imdb sc0re' : 'imdb_score',
    'imdb v0tes' : 'imdb_votes'
    }
)

## Task 2: Correcting a Misspelled Name in the Data
df.loc[df['name'] == 'In??s Prieto']

Correct the name

df.loc[77798, 'name'] = 'Ines Prieto'
df.loc[85576, 'name'] = 'Ines Prieto'

Verify the correction

display(df.loc[77798, 'name'])
df.loc[85576, 'name']
df.loc[df['name'] == 'In??s Prieto']


## Task 3: Finding All Movies and Shows Featuring Ines Prieto
ines_prieto = df[df['name'] == 'Ines Prieto']
ines_prieto = ines_prieto[['title', 'release_year', 'imdb_score', 'genres']]
ines_prieto
ines_prieto = ines_prieto.drop_duplicates()
ines_prieto


## Task 4: Finding Highly Rated Movies
high_score = df[df['imdb_score'] > 9]
high_score_title = high_score['title']
unique_titles = set(high_score_title)
unique_titles


## Task 5: Creating a Function to Find Unique Top-Rated Movies
def get_unique_top_movies(min_score):
    high_score_df = df[df['imdb_score'] > min_score]
    high_score_titles = high_score_df['title']
    high_score_unique_titles = set(high_score_titles)
    return high_score_unique_titles


## Task 6: Creating a Function to Find Top Movies from a Specific Decade
def get_top_movies_from_decade(decade_start, min_score):
    by_decade = df[(df['release_year'] >= decade_start) & (df['release_year'] <= (decade_start + 9))]
    by_score = by_decade[by_decade['imdb_score'] >= min_score]
    only_titles = by_score['title']
    unique_titles = set(only_titles)
    return unique_titles


## Task 7: Creating a Function to List All Actors in a Given Title
def get_actors_for_title(title):
    filtered_df = df[(df['title'] == title) & (df['role'] == 'ACTOR')]
    names = filtered_df['name']
    listed = ', '.join(names)
    return listed


## Task 8: Creating a Function to Categorize Movies by IMDb Score
def categorize_imdb_score(title):
    filtered_df = df[df['title'] == title]
    if not filtered_df.empty:
        imdb_score = filtered_df['imdb_score'].values[0]
        if imdb_score >= 9.0:
            return 'Excellent'
        elif 7.0 <= imdb_score <= 8.9:
            return 'Good'
        elif 5.0 <= imdb_score <= 6.9:
            return 'Average'
        else:
            return 'Low'
    else:
        return 'Title not found'
</p>

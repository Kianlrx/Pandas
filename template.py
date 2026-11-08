#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

"""
    Created on Fri Oct 23 12:16:36 2026

    Your Full Name: Kian le Roux
    
    Your Student ID: R00268281
    
    Your Cohort: SDH3-A
"""

# defining columns labels
columns = ['name', 'date', 'imdb_score', 'country', 'language', 'director', 'type', 'no_critics', 'duration_mins', 'gross_cost', 'genres', 'no_votes', 'keywords', 'first_actor', 'no_director_fb_likes', 'no_actor_fb_likes']
# records list will hold a 2D matrix of parsed data from text file
records = []

with open("ExtractedInput.txt", "r", encoding="UTF8") as file: # UTF8 to account for unrecognised chars in text file
    for line in file:
        real_line = line.rstrip()

        if not real_line: # skip all lines between records that contain nothing
            continue

        row_values = [] # list for each movie entry in text file

        segments = line.strip().split(" -- ") # each value in text file separated by " -- "
        for segment in segments:
            # splitting each segment by the ':'
            if ':' in segment: # to account for some records not containing ':'
                _, value = segment.split(":", 1) # maxsplit = 1 because some movie titles etc. contain the char ':'
                row_values.append(value.strip())

        records.append(row_values)

movie_df = pd.DataFrame(records, columns=columns)

# extracting numerical data from values that contain strings
unit_cols = ["duration_mins", "no_director_fb_likes", "no_actor_fb_likes"]
for col in unit_cols:
    movie_df[col] = movie_df[col].str.extract(r"([\d.]+)").astype(float)

# convert series to contain appropriate data types
movie_df["date"] = pd.to_datetime(movie_df["date"], errors="coerce")
movie_df["imdb_score"] = pd.to_numeric(movie_df["imdb_score"], errors='coerce')
movie_df["no_critics"] = pd.to_numeric(movie_df["no_critics"], errors='coerce')
movie_df["gross_cost"] = pd.to_numeric(movie_df["gross_cost"], errors='coerce')
movie_df["no_votes"] = pd.to_numeric(movie_df["no_votes"], errors='coerce')


#movie_df.info()

movie_df.to_csv("film.csv")


def task1():
    # sort the dataframe by date and set date as the index
    df_sorted = movie_df.sort_values("date").set_index("date")

    plt.figure(figsize=(10, 5))

    # scale gross cost to 'millions'
    gross_in_millions = df_sorted["gross_cost"] / 1_000_000

    # scatter plot
    plt.scatter(df_sorted.index, gross_in_millions, alpha=0.5)

    plt.xlabel("Date")
    plt.ylabel("Gross Cost (Millions $)")
    plt.title("Movie Gross Cost Over Time")

    plt.tight_layout()
    plt.show()

    """
        I chose a scatter plot because it does a good job at showing
        where each individual movie sits on the graph while also showing
        us how where the majority of values lie while also showing outliers.
    """
    
def task2(): # Movie Frequency Per Year

    # create series with the year versions of each datetime value in the "dates" series
    year_counts = movie_df['date'].dt.year.value_counts()
    year_counts = year_counts.sort_index() # creating a sorted version of the new series

    # line plot
    plt.figure(figsize=(10, 5))
    plt.plot(year_counts.index, year_counts.values)

    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Movie Year Frequency Distribution (All Time)")

    plt.tight_layout()
    plt.show()

    """ 
        I chose a time series plot because it displays a nice line that
        depicts the trend 
    """
def task3(): # 1950 - 2010 Movie Frequency

    # create a new dataframe only containing movies where date: 1950 - 2010
    filtered_df = movie_df[(movie_df["date"].dt.year >= 1950) & (movie_df["date"].dt.year <= 2010)]

    year_counts = filtered_df["date"].dt.year.value_counts() # new series containing frequency values (year is UDI)
    year_counts = year_counts.sort_index()  # creating a sorted version of the new series

    # line plot
    plt.figure(figsize=(10, 5))
    plt.plot(year_counts.index, year_counts.values)

    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Movie Year Frequency Distribution (1950 - 2010)")

    plt.tight_layout()
    plt.show()

    """
        From the generated graph, the frequency of movie releases gradually rises
        from the year 1950 until approximately 1993 and then experiences a sudden
        increase in frequency which continues up until the end of the graph (2010)
    """
    
def task4():

    # Creating pandas series for each grouping
    group1 = (
            movie_df['genres'].str.contains(
                'Action|Adventure', na=False
            ) &
            movie_df['genres'].str.contains(
                'Thriller|Western', na=False
            )
    )

    group2 = (
            movie_df['genres'].str.contains(
                'Action|Adventure', na=False
            ) &
            movie_df['genres'].str.contains(
                'Fantasy|Family', na=False
            )
    )

    group3 = (
            movie_df['genres'].str.contains(
                'Fantasy|Family', na=False
            ) &
            movie_df['genres'].str.contains(
                'Sci-Fi|Comedy', na=False
            )
    )

    # create dataframe from each group
    group1_df = movie_df[group1]
    group2_df = movie_df[group2]
    group3_df = movie_df[group3]

    # create a python list which contains mean duration values for each group
    average_durations = [
        group1_df['duration_mins'].mean(),
        group2_df['duration_mins'].mean(),
        group3_df['duration_mins'].mean()
    ]

    # bar chart to visualise data
    plt.figure(figsize=(10, 5))

    plt.bar(
        ['Group 1', 'Group 2', 'Group 3'],
        average_durations
    )

    plt.xlabel('Genre Combination')
    plt.ylabel('Average Duration (Minutes)')
    plt.title('Average Movie Duration by Genre Combination')

    plt.tight_layout()
    plt.show()

    """
        Each bar in the bar chart represents the average duration for all movies that have at least 1 genre
        from each sub group.
        
        Group 1: Action, Adventure + Thriller, Western
        Group 2: Action, Adventure + Fantasy, Family
        Group 3: Fantasy, Family + Sci-Fi, Comedy
        
        Casino Royale: Action, Adventure, Thriller --> Group 1
        Harry Potter and the Order of the Phoenix: Adventure, Family, Fantasy, Mystery --> Group 2
        Ghostbusters: Comedy, Fantasy, Sci-Fi --> Group 3
        The Notebook: Drama, Romance --> None
        Night at the Museum: Action, Adventure, Comedy, Family, Fantasy --> Group 2 and Group 3
    """

def task5():
    # define keyword categories
    crime_keywords = movie_df['keywords'].str.contains(
        'criminal|prison|gang', na=False
    )

    science_keywords = movie_df['keywords'].str.contains(
        'science|math|computer', na=False
    )

    # create dataframes containing the filtered data
    crime_df = movie_df[crime_keywords]
    science_df = movie_df[science_keywords]

    # create series with UDI of country and value of count
    crime_countries = crime_df['country'].value_counts()
    science_countries = science_df['country'].value_counts()

    # top 6 countries to be visualised on the graph
    crime_top6 = crime_countries.head(6)
    science_top6 = science_countries.head(6)

    # Crime Bar Chart
    plt.figure(figsize=(10, 5))

    plt.barh(crime_top6.index, crime_top6.values)
    plt.xlabel('Number of Movies')
    plt.ylabel('Country')
    plt.title('Top 6 Countries for Crime-Related Movies')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    # Science Bar Chart
    plt.figure(figsize=(10, 5))

    plt.barh(science_top6.index, science_top6.values)
    plt.xlabel('Number of Movies')
    plt.ylabel('Country')
    plt.title('Top 6 Countries for Science-Related Movies')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    """
    My takeaway from the plotted graphs is that since the USA make so many movies relative to other countries,
    they will be leading in frequency regardless of the keywords. A better approach might be to display the
    number of movies as a percentage of the amount of movies that country has produced. This would better show
    any trends or patterns as the current graphs seem to only display the countries that make the most movies.
    """

def task6(): # bar chart of top 7 most popular genres (frequency on the 7-axis)

    # split each movie's genres into individual genres
    genres = movie_df['genres'].str.split('|')

    # convert the lists into individual rows
    all_genres = genres.explode()

    # count how frequently each genre appears
    genre_counts = all_genres.value_counts()

    # get the 7 most common genres
    top7_genres = genre_counts.head(7)

    # Bar chart
    plt.figure(figsize=(10, 5))

    plt.bar(top7_genres.index, top7_genres.values)

    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.title('Top 7 Most Common Movie Genres')

    plt.tight_layout()
    plt.show()
    
def task7(): # bar chart of most successful directors based on average movie ratings

    # group movies by director and calculate average score and movie count
    director_stats = movie_df.groupby('director')['imdb_score'].agg(['mean', 'count'])

    # exclude directors with fewer than 5 movies to remove one-trick-ponies
    director_stats = director_stats[director_stats['count'] >= 5]

    # sort by average score
    director_stats = director_stats.sort_values('mean', ascending=False)

    top6_directors = director_stats.head(6)
    bottom6_directors = director_stats.tail(6)

    # bar chart of best directors
    plt.figure(figsize=(10, 5))
    plt.bar(top6_directors.index, top6_directors['mean'])
    plt.xlabel('Director')
    plt.ylabel('Average Movie Score')
    plt.title('Top 6 Directors by Average Movie Score')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # bar chart of worst directors
    plt.figure(figsize=(10, 5))
    plt.bar(bottom6_directors.index, bottom6_directors['mean'])
    plt.xlabel('Director')
    plt.ylabel('Average Movie Score')
    plt.title('Top 6 Directors by Average Movie Score')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

task1()
task2()
task3()
task4()
task5()
task6()
task7()
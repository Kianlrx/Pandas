#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
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
#-------------------------------------------------------------------------------------
print(f"First 4 Records:\n{records[0]}\n{records[1]}\n{records[2]}\n{records[3]}\n\n")
#-------------------------------------------------------------------------------------

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

movie_df.info()

# save the dataframe as film.csv


#def task1():
    
    # your implementation goes here.
    
    
    
#def task2():
    
    # your implementation goes here.
    
    
#def task3():
    
    # your implementation goes here.
    
    
#def task4():
    
    # your implementation goes here.
    
    
#def task5():
    
    # your implementation goes here.
    
#def task6():
    
    # your implementation goes here.
    
#def task7():
    
    # your implementation goes here.
    
    


#task1()
#task2()
#task3()
#task4()
#task5()
#task6()
#task7()




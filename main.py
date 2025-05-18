# This Python project implements a basic recommender system using pandas to suggest items similar to a chosen item,
# specifically movies. The code focuses on identifying movies most similar to a given movie choice. Note that this is
# a simplified system and not a fully robust recommender system. This project contains the core functionality
# for basic movie recommendations.


# 1. Import Libraries
# 1.1 Imports numpy to handle numbers for data work with pandas
import numpy as np

# 1.2 Sets numpy to ignore invalid operation warnings to avoid correlation errors
np.seterr(all='warn')  # Warns but doesn’t stop for invalid operations like divide by zero

# 1.3 Imports pandas to load and analyze data in tables
import pandas as pd

# 1.4 Imports matplotlib.pyplot to create graphs for data visualization
import matplotlib.pyplot as plt

# 1.5 Imports seaborn to make prettier plots for data analysis
import seaborn as sns

# 1.6 Sets a clean white style for plots to look professional
sns.set_style('white')


# 2. Get the Data
# 2.1 Creates a list of column names for the ratings data file
column_names = ['user_id', 'item_id', 'rating', 'timestamp']

# 2.2 Loads the tab-separated ratings file into a table for analysis
df = pd.read_csv('u.data', sep='\t', names=column_names)


# 3. Load Movie Titles
# 3.1 Loads the movie titles file into a table to get names for movie IDs
movie_titles = pd.read_csv("Movie_Id_Titles")


# 4. Merge Data
# 4.1 Combines ratings and movie titles tables using movie IDs
df = pd.merge(df, movie_titles, on='item_id')


# 5. Exploratory Data Analysis
# 5.1 Calculates average rating per movie and sorts them to find top-rated movies
avg_ratings = df.groupby('title')['rating'].mean().sort_values(ascending=False)

# 5.2 Shows the top 5 movies with highest average ratings
print("Top 5 movies by average rating:\n", avg_ratings.head())

# 5.3 Counts ratings per movie and sorts them to find most-rated movies
rating_counts = df.groupby('title')['rating'].count().sort_values(ascending=False)

# 5.4 Shows the top 5 movies with the most ratings
print("\nTop 5 movies by number of ratings:\n", rating_counts.head())

# 5.5 Creates a table with average ratings per movie for analysis
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

# 5.6 Adds a column with the number of ratings per movie to the table
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())


# 6. Visualize Data
# 6.1 Sets the plot size to 10x4 inches for clear visualization
plt.figure(figsize=(10, 4))

# 6.2 Plots a histogram of rating counts to show how many ratings movies have
ratings['num of ratings'].hist(bins=70)

# 6.3 Adds a title to the histogram to explain the chart
plt.title('Distribution of Number of Ratings')

# 6.4 Labels the x-axis to show it represents the number of ratings
plt.xlabel('Number of Ratings')

# 6.5 Labels the y-axis to show it represents the count of movies
plt.ylabel('Frequency')

# 6.6 Saves the histogram as an image file for viewing in PyCharm
plt.savefig('num_ratings_hist.png')

# 6.7 Closes the plot to free memory and avoid overlapping
plt.close()

# 6.8 Sets the plot size to 10x4 inches for clear visualization
plt.figure(figsize=(10, 4))

# 6.9 Plots a histogram of average ratings to show their distribution
ratings['rating'].hist(bins=70)

# 6.10 Adds a title to the histogram to explain the chart
plt.title('Distribution of Average Ratings')

# 6.11 Labels the x-axis to show it represents the average rating
plt.xlabel('Average Rating')

# 6.12 Labels the y-axis to show it represents the count of movies
plt.ylabel('Frequency')

# 6.13 Saves the histogram as an image file for viewing in PyCharm
plt.savefig('avg_ratings_hist.png')

# 6.14 Closes the plot to free memory and avoid overlapping
plt.close()

# 6.15 Creates a scatter plot with histograms to show ratings vs. number of ratings
joint_plot = sns.jointplot(x='rating', y='num of ratings', data=ratings, alpha=0.5)

# 6.16 Adds a title to the scatter plot to explain the chart
joint_plot.fig.suptitle('Ratings vs. Number of Ratings')

# 6.17 Labels the axes to show average rating and number of ratings
joint_plot.set_axis_labels('Average Rating', 'Number of Ratings')

# 6.18 Saves the scatter plot as an image file for viewing in PyCharm
plt.savefig('joint_plot.png')

# 6.19 Closes the plot to free memory and avoid overlapping
plt.close()


# 7. Build Recommendation System
# 7.1 Creates a matrix of user ratings for movies to compare them
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

# 7.2 Sorts movies by number of ratings to find popular ones for recommendations
top_rated = ratings.sort_values('num of ratings', ascending=False)

# 7.3 Shows the top 10 movies with the most ratings
print("\nTop 10 most rated movies:\n", top_rated.head(10))

# 7.4 Extracts ratings for Star Wars to find similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']

# 7.5 Extracts ratings for Liar Liar to find similar movies
liarliar_user_ratings = moviemat['Liar Liar (1997)']

# 7.6 Finds how other movies' ratings match with Star Wars to identify similar ones
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

# 7.7 Finds how other movies' ratings match with Liar Liar to identify similar ones
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

# 7.8 Turns Star Wars correlations into a table to organize similarity scores
corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])

# 7.9 Removes rows with missing correlations to clean the data
corr_starwars.dropna(inplace=True)

# 7.10 Adds rating counts to the Star Wars correlations table to filter popular movies
corr_starwars = corr_starwars.join(ratings['num of ratings'])

# 7.11 Keeps movies with 100+ ratings and sorts them to recommend similar ones to Star Wars
starwars_recommendations = corr_starwars[corr_starwars['num of ratings'] > 100].sort_values('Correlation', ascending=False)

# 7.12 Shows the top 5 movies similar to Star Wars
print("\nTop 5 movies similar to Star Wars (1977):\n", starwars_recommendations.head())

# 7.13 Turns Liar Liar correlations into a table to organize similarity scores
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])

# 7.14 Removes rows with missing correlations to clean the data
corr_liarliar.dropna(inplace=True)

# 7.15 Adds rating counts to the Liar Liar correlations table to filter popular movies
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])

# 7.16 Keeps movies with 100+ ratings and sorts them to recommend similar ones to Liar Liar
liarliar_recommendations = corr_liarliar[corr_liarliar['num of ratings'] > 100].sort_values('Correlation', ascending=False)

# 7.17 Shows the top 5 movies similar to Liar Liar
print("\nTop 5 movies similar to Liar Liar (1997):\n", liarliar_recommendations.head())

# 5. Exploratory Data Analysis
# 5.1 Calculates average rating per movie and sorts them to find top-rated movies
avg_ratings = df.groupby('title')['rating'].mean().sort_values(ascending=False)

# 5.2 Shows the top 5 movies with highest average ratings
print("Top 5 movies by average rating:\n", avg_ratings.head())

# 5.3 Counts ratings per movie and sorts them to find most-rated movies
rating_counts = df.groupby('title')['rating'].count().sort_values(ascending=False)

# 5.4 Shows the top 5 movies with the most ratings
print("\nTop 5 movies by number of ratings:\n", rating_counts.head())

# 5.5 Creates a table with average ratings per movie for analysis
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

# 5.6 Adds a column with the number of ratings per movie to the table
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())



# 6. Visualize Data
# 6.1 Sets the plot size to 10x4 inches for clear visualization
plt.figure(figsize=(10, 4))

# 6.2 Plots a histogram of rating counts to show how many ratings movies have
ratings['num of ratings'].hist(bins=70)

# 6.3 Adds a title to the histogram to explain the chart
plt.title('Distribution of Number of Ratings')

# 6.4 Labels the x-axis to show it represents the number of ratings
plt.xlabel('Number of Ratings')

# 6.5 Labels the y-axis to show it represents the count of movies
plt.ylabel('Frequency')

# 6.6 Saves the histogram as an image file for viewing in PyCharm
plt.savefig('num_ratings_hist.png')

# 6.7 Closes the plot to free memory and avoid overlapping
plt.close()

# 6.8 Sets the plot size to 10x4 inches for clear visualization
plt.figure(figsize=(10, 4))

# 6.9 Plots a histogram of average ratings to show their distribution
ratings['rating'].hist(bins=70)

# 6.10 Adds a title to the histogram to explain the chart
plt.title('Distribution of Average Ratings')

# 6.11 Labels the x-axis to show it represents the average rating
plt.xlabel('Average Rating')

# 6.12 Labels the y-axis to show it represents the count of movies
plt.ylabel('Frequency')

# 6.13 Saves the histogram as an image file for viewing in PyCharm
plt.savefig('avg_ratings_hist.png')

# 6.14 Closes the plot to free memory and avoid overlapping
plt.close()

# 6.15 Creates a scatter plot with histograms to show ratings vs. number of ratings
joint_plot = sns.jointplot(x='rating', y='num of ratings', data=ratings, alpha=0.5)

# 6.16 Adds a title to the scatter plot to explain the chart
joint_plot.fig.suptitle('Ratings vs. Number of Ratings')

# 6.17 Labels the axes to show average rating and number of ratings
joint_plot.set_axis_labels('Average Rating', 'Number of Ratings')

# 6.18 Saves the scatter plot as an image file for viewing in PyCharm
plt.savefig('joint_plot.png')

# 6.19 Closes the plot to free memory and avoid overlapping
plt.close()



# 7. Build Recommendation System
# 7.1 Creates a matrix of user ratings for movies to compare them
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

# 7.2 Sorts movies by number of ratings to find popular ones for recommendations
top_rated = ratings.sort_values('num of ratings', ascending=False)

# 7.3 Shows the top 10 movies with the most ratings
print("\nTop 10 most rated movies:\n", top_rated.head(10))

# 7.4 Extracts ratings for Star Wars to find similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']

# 7.5 Extracts ratings for Liar Liar to find similar movies
liarliar_user_ratings = moviemat['Liar Liar (1997)']

# 7.6 Finds how other movies' ratings match with Star Wars to identify similar ones
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

# 7.7 Finds how other movies' ratings match with Liar Liar to identify similar ones
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

# 7.8 Turns Star Wars correlations into a table to organize similarity scores
corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])

# 7.9 Removes rows with missing correlations to clean the data
corr_starwars.dropna(inplace=True)

# 7.10 Adds rating counts to the Star Wars correlations table to filter popular movies
corr_starwars = corr_starwars.join(ratings['num of ratings'])

# 7.11 Keeps movies with 100+ ratings and sorts them to recommend similar ones to Star Wars
starwars_recommendations = corr_starwars[corr_starwars['num of ratings'] > 100].sort_values('Correlation', ascending=False)

# 7.12 Shows the top 5 movies similar to Star Wars
print("\nTop 5 movies similar to Star Wars (1977):\n", starwars_recommendations.head())

# 7.13 Turns Liar Liar correlations into a table to organize similarity scores
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])

# 7.14 Removes rows with missing correlations to clean the data
corr_liarliar.dropna(inplace=True)

# 7.15 Adds rating counts to the Liar Liar correlations table to filter popular movies
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])

# 7.16 Keeps movies with 100+ ratings and sorts them to recommend similar ones to Liar Liar
liarliar_recommendations = corr_liarliar[corr_liarliar['num of ratings'] > 100].sort_values('Correlation', ascending=False)

# 7.17 Shows the top 5 movies similar to Liar Liar
print("\nTop 5 movies similar to Liar Liar (1997):\n", liarliar_recommendations.head())
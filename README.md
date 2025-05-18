# Movie Recommendation System

This project builds a simple movie recommendation system using Python and the MovieLens 100k dataset. It suggests movies similar to "Star Wars (1977)" and "Liar Liar (1997)" based on user ratings. The code also analyzes movie ratings and creates visualizations to explore data patterns.

## Project Overview

The system:
- Loads user ratings and movie titles from the MovieLens 100k dataset.
- Merges data to associate ratings with movie names.
- Analyzes top-rated and most-rated movies.
- Creates visualizations (histograms and scatter plot) to show rating distributions.
- Uses correlation to recommend movies similar to "Star Wars" and "Liar Liar."

The code is written in Python, runs in PyCharm, and is organized into seven steps with clear comments for beginners.

## Requirements

- **Python 3.8+**
- **Libraries**:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
- **Data Files**:
  - `u.data`: User ratings (tab-separated).
  - `Movie_Id_Titles`: Movie IDs and titles.
  - Download from [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/).

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ibryam/recommender-systems.git
   cd recommender-systems

Install Dependencies:
In PyCharm’s terminal or your command line, run:
bash

pip install numpy pandas matplotlib seaborn

Add Data Files:
Place u.data and Movie_Id_Titles in the project root (recommender-systems/).

If missing, download the MovieLens 100k dataset from GroupLens.

Extract u.data and u.item (rename u.item to Movie_Id_Titles with columns item_id and title).

Project Structure:

recommender-systems/
├── movie_recommender.py
├── u.data
├── Movie_Id_Titles
├── num_ratings_hist.png
├── avg_ratings_hist.png
├── joint_plot.png
├── README.md

Running the Code
Open movie_recommender.py in PyCharm.

Right-click the file and select Run.

The script will:
Print top 5 movies by average rating and number of ratings.

Print top 10 most-rated movies.

Print top 5 recommendations for "Star Wars (1977)" and "Liar Liar (1997)".

Save three visualizations as PNG files in the project directory.

Visualizations
The script generates three plots to explore the data:
Histogram of Number of Ratings:
Shows how many ratings movies have (most have few, some have many).
Number of Ratings Histogram

Histogram of Average Ratings:
Shows the distribution of average movie ratings (most are around 3-4 stars).
Average Ratings Histogram

Scatter Plot of Ratings vs. Number of Ratings:
Shows the relationship between average ratings and number of ratings.
Ratings vs. Number of Ratings


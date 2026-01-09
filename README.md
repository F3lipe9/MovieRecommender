# Movie Recommender

A Python-based movie recommendation system that suggests similar movies based on genre preferences and runtime constraints.

## Features

- **Genre-Based Recommendations**: Finds movies with similar genres to your input movie
- **Runtime Filtering**: Filters recommendations based on your maximum movie length preference
- **Top 10 Results**: Returns the top 10 highest-rated movies matching your criteria
- **IMDB Data**: Uses a dataset of 1000 movies with ratings, genres, and runtime information

## How It Works

1. User inputs a movie title they enjoyed
2. User specifies the maximum runtime they're willing to watch
3. The system identifies the genres of the input movie
4. Filters movies by:
   - Shared genres with the input movie
   - Runtime less than or equal to the specified maximum
5. Sorts results by IMDB rating (highest first)
6. Returns the top 10 recommendations

## Requirements

- Python 3.x
- pandas library

## Installation

```bash
pip install pandas
```

## Usage

Run the program:

```bash
python main.py
```

Example interaction:

```
What Movie Do You Want To Find Something Similar? Prometheus
Whats The Longest Movie Time Are You Feeling? 150

Genres for 'Prometheus': Adventure,Mystery,Sci-Fi

Recommended Movies:
[Top 10 movies displayed with Title, Genre, Runtime, and Rating]
```

## Data Source

The program uses `IMDB-Movie-Data.csv` containing information about 1000 movies including:
- Title
- Genre
- Runtime (Minutes)
- Rating
- Year
- Votes

## Project Structure

```
movieRecomender/
├── main.py                 # Main application code
├── IMDB-Movie-Data.csv    # Movie dataset
└── README.md              # This file
```

## Functions

- `create_and_clean_Data()`: Loads and preprocesses the movie dataset
- `findRecommendation(df)`: Finds and returns top 10 movie recommendations based on user input

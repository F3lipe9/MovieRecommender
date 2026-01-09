import pandas as pd

userMovie = str(input("What Movie Do You Want To Find Something Similar? "))
userTime = int(input("Whats The Longest Movie Time Are You Feeling? "))



def create_and_clean_Data():
    df = pd.read_csv("IMDB-Movie-Data.csv")

    # Total Movies = 1000
    # Longest Movie = 191 Minutes
    # Shortest Movie = 66 Minutes

    # Convert Runtime to numeric, coercing errors to NaN
    df["Runtime (Minutes)"] = pd.to_numeric(df["Runtime (Minutes)"], errors='coerce')
    return df.drop(columns=["Revenue (Millions)", "Director", "Actors", "Description", "Metascore", "Rank"])

def findRecommendation(df):
    # Find the movie
    movieRow = df[df["Title"] == userMovie]

    if movieRow.empty:
        print(f"Movie '{userMovie}' not found in database.")
        return pd.DataFrame()

    # Extract genres
    genres = movieRow["Genre"].values[0]
    print(f"Genres for '{userMovie}': {genres}")

    # Filter by runtime
    df = df[df["Runtime (Minutes)"] <= userTime]

    # Filter by shared genre keyword
    genre_keywords = genres.split(", ")
    df = df[df["Genre"].apply(lambda g: any(keyword in g for keyword in genre_keywords))]

    # Remove the original movie
    df = df[df["Title"] != userMovie]

    # Sort by rating (optional)
    df = df.sort_values(by="Rating", ascending=False)

    # Get Top 10
    df = df.head(10)

    return df[["Title", "Genre", "Runtime (Minutes)", "Rating"]]

df = create_and_clean_Data()
recommendations = findRecommendation(df)


print("\nRecommended Movies:")
print(recommendations.to_string())





    
import pandas as pd

# Load dataset
df = pd.read_csv("movies.csv")

print("===== Movie Recommendation System =====")

# Display available genres
print("\nAvailable Genres:")
print(df["Genre"].unique())

# Take user input
genre = input("\nEnter your favorite genre: ")

# Find matching movies
recommended = df[df["Genre"].str.lower() == genre.lower()]

# Display recommendations
if len(recommended) > 0:
    print("\nRecommended Movies:\n")

    for movie in recommended["Movie"]:
        print("-", movie)

else:
    print("\nSorry! No movies found for this genre.")
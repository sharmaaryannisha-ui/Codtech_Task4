# Movie Recommendation System using Python

A simple Python-based Movie Recommendation System that suggests movies based on user-selected genres using a CSV dataset and Pandas.

## Features
- Load movie dataset from CSV file
- Display available genres
- Take user input for favorite genre
- Filter movies based on selected genre
- Display recommended movies list
- Handle cases where no movies are found

## Technologies Used
- Python 3
- Pandas

## Project Structure
```
Movie-Recommendation-System/
│── movies.csv
│── movie_recommendation.py
└── README.md
```

## Dataset Format
The `movies.csv` file should contain at least two columns:

- Movie → Name of the movie  
- Genre → Genre of the movie  

Example:
```
Movie,Genre
Inception,Sci-Fi
Titanic,Romance
Avengers,Action
```

## Installation
Install required library:

```bash
pip install pandas
```

## Usage
Run the Python script:

```bash
python movie_recommendation.py
```

Then enter your favorite genre when prompted.

## Output
- List of recommended movies based on selected genre
- Message if no movies are found

## Example
```
Enter your favorite genre: Action

Recommended Movies:
- Avengers
- John Wick
- Mad Max
```

## Author
**Aryan Sharma**

## License
This project is open-source and free to use.

# Movie Data Analysis Project

## Overview

This project uses Python and the Pandas library to process, analyse and visualise a dataset containing information about movies.

The dataset is initially provided in a text file (`ExtractedInput.txt`), which is parsed and converted into a Pandas DataFrame. The data is then cleaned, converted into appropriate data types and exported to a CSV file for further use.

Several analytical tasks are performed to identify trends and patterns in the movie industry, using IMDb ratings, release dates, genres, countries, directors and other movie-related information.

## Technologies Used

- **Python 3** – Main programming language.
- **Pandas** – Data processing, cleaning, filtering and analysis.
- **NumPy** – Numerical operations.
- **Matplotlib** – Data visualisation.

## Project Structure

```text
Movie-Data-Analysis/
│
├── ExtractedInput.txt    # Original movie dataset
├── film.csv              # Processed dataset
├── main.py               # Main Python script
└── README.md             # Project documentation
```

## Data Processing

The original text file is parsed line by line, with individual movie attributes extracted and stored in a Pandas DataFrame.

The following preprocessing operations are performed:

- Empty lines are ignored.
- Movie attributes are extracted from the original text file.
- Numerical values are extracted from fields containing units.
- Date values are converted into datetime objects.
- Numerical columns are converted into appropriate numeric data types.
- The cleaned dataset is exported to `film.csv`.

## Analysis Tasks

The project contains seven analytical tasks, each using different data analysis techniques and visualisations.

### Task 1 – Movie Gross Revenue Over Time
A scatter plot displaying movie gross revenue across different release dates. This helps identify trends, distributions and potential outliers.

### Task 2 – Movie Frequency Per Year
A time-series line graph showing the number of movies released each year across the entire dataset.

### Task 3 – Movie Frequency Between 1950 and 2010
A filtered time-series graph showing the frequency of movie releases between 1950 and 2010.

### Task 4 – Average Movie Duration by Genre Combination
Compares the average duration of movies belonging to three different genre combinations:

- Action / Adventure + Thriller / Western
- Action / Adventure + Fantasy / Family
- Fantasy / Family + Sci-Fi / Comedy

Movies can belong to multiple groups if they satisfy the relevant genre conditions.

### Task 5 – Countries Producing Crime and Science-Related Movies
Identifies the six countries with the highest number of movies containing crime-related and science-related keywords.

Two separate horizontal bar charts are generated to visualise the results.

### Task 6 – Seven Most Popular Movie Genres
Identifies the seven most frequently occurring genres across the dataset.

Genre values are separated into individual categories before being counted, allowing movies with multiple genres to contribute to each relevant category.

### Task 7 – Most Successful Directors by Average IMDb Rating
Calculates the average IMDb rating for each director and identifies the six highest-ranking directors.

To improve the reliability of the comparison, directors must have at least five movies in the dataset to qualify.

## Installation and Requirements

Make sure Python 3 is installed on your system.

Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib
```

## Running the Project

1. Clone or download the project.
2. Ensure `ExtractedInput.txt` is located in the same directory as the Python script.
3. Install the required Python libraries.
4. Run the main Python script:

```bash
python main.py
```

The script will process the dataset, generate `film.csv` and display the visualisations for all seven analytical tasks.

## Output

The project generates:

- A cleaned CSV file containing the processed movie dataset.
- Seven analytical tasks.
- Multiple visualisations, including scatter plots, line graphs and bar charts.


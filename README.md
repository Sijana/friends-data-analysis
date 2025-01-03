![alt text](/cover-image.png)


# Friends Episodes Data Analysis

## Overview
This repository contains data analysis of the TV show *Friends*, focusing on understanding patterns and insights from episodes across all seasons. The analysis includes examining episode ratings, character lines, scene counts, and other metadata to explore factors influencing episode popularity, trends in character appearances, and more.

## Project Structure
- **Data Collection**: The dataset combines character dialogue, scene counts, episode titles, ratings, and metadata such as directors, writers, and original air dates.
- **Data Cleaning and Processing**: Data is cleaned and processed to handle typos in character names, consolidate episode metadata, and structure the data to support analysis.
- **Analysis and Visualizations**: The project includes various analyses, such as character line counts, scene counts, ratings trends, and factors influencing episode ratings.

## Data Sources
- **Character Lines and Scene Counts**: Derived from text files containing episode scripts. Scene counts per character are calculated by identifying each character’s participation in scenes.
- **Episode Metadata**: Episode information, ratings, and viewer statistics collected from online databases.

## Repository Contents
- `data/`: Contains raw data files for analysis.
- `output/`: Contains the processed data generated by preprocessing script.
- `scripts/`: Includes Python scripts for data cleaning and preprocessing.
- `friends_episodes/`: Includes scripts of all episodes.
- `notebooks/`: Jupyter notebook demonstrating data processing and analysis steps.
- `README.md`: Project documentation (this file).

## Key Analysis
- **Character Appearances**: Counts the number of lines and scenes for each main character per episode and season.
- **Character Sentiment**: Looks at changes in sentiment across seasons for main characters ad
sees if there is any significant differences between the overall candidate sentiment.
- **Rating Influences**: Analyzes factors such as character involvement, episode duration, director, and viewership to identify correlations with episode ratings.
- **Visualizations**: Plots episode ratings, line counts vs. scene counts, and character trends to explore relationships within the data.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Required libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt

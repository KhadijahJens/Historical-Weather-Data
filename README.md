Weather Data Processing Program

# Description
This Python program processes historical weather data from https://open-meteo.com/en/docs/historical-weather-api and
stores it in a SQLite database. It provides functionality to add new weather data, query existing data,
and perform basic analysis.

# Installation
1. Clone the repository:
git clone https://gitlab.com/wgu-gitlab-environment/student-repos/kjens1/d493-scripting-and-programming-applications.git

2. Install the required dependencies:
pip install -r requirements.txt


# Commands
- python main.py : Runs the program to retrieve weather data from the API and store it in the database.

# Inputs
- API key from the weather service provider

# Outputs
- The program will fetch weather data from the API and store it in a SQLite database named weather_data.db.
- It will also provide options to fetch new weather data, query existing data, and perform basic analysis.

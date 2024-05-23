# Climate Analysis API

This project provides a Flask API to perform climate analysis on a SQLite database containing weather data. The API includes various endpoints to retrieve precipitation data, weather station information, temperature observations, and temperature statistics.

## Project Structure


- `app.py`: The main Flask application file that sets up the API routes and connects to the SQLite database.
- `hawaii.sqlite`: The SQLite database file containing the weather data.
- `README.md`: This README file.

## Getting Started



## Available Routes

- **Homepage**:
  - **URL**: `/`
  - **Description**: Lists all available API routes.

- **Precipitation Data**:
  - **URL**: `/api/v1.0/precipitation`
  - **Description**: Returns the last 12 months of precipitation data in JSON format.

- **Stations**:
  - **URL**: `/api/v1.0/stations`
  - **Description**: Returns a JSON list of all weather stations.

- **Temperature Observations**:
  - **URL**: `/api/v1.0/tobs`
  - **Description**: Returns the temperature observations for the last 12 months for the most active station in JSON format.

- **Temperature Statistics for a Start Date**:
  - **URL**: `/api/v1.0/<start>`
  - **Description**: Returns the minimum, average, and maximum temperatures from the start date to the most recent date in JSON format.
  - **Example**: `/api/v1.0/2017-01-01`

- **Temperature Statistics for a Date Range**:
  - **URL**: `/api/v1.0/<start>/<end>`
  - **Description**: Returns the minimum, average, and maximum temperatures for the specified date range in JSON format.
  - **Example**: `/api/v1.0/2017-01-01/2017-12-31`

## Example Usage

- **Homepage**:
  - Open your web browser and go to `http://127.0.0.1:5000/`
  - You should see a welcome message listing all the available routes.

- **Precipitation Data**:
  - Go to `http://127.0.0.1:5000/api/v1.0/precipitation`
  - This route returns the last 12 months of precipitation data in JSON format.

- **Stations**:
  - Go to `http://127.0.0.1:5000/api/v1.0/stations`
  - This route returns a list of all weather stations in JSON format.

- **Temperature Observations**:
  - Go to `http://127.0.0.1:5000/api/v1.0/tobs`
  - This route returns the temperature observations for the last 12 months for the most active station in JSON format.

- **Temperature Statistics for a Start Date**:
  - Go to `http://127.0.0.1:5000/api/v1.0/2017-01-01`
  - This route returns the minimum, average, and maximum temperatures from the start date to the most recent date in JSON format.

- **Temperature Statistics for a Date Range**:
  - Go to `http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31`
  - This route returns the minimum, average, and maximum temperatures for the specified date range in JSON format.



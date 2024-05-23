# Climate Analysis API

## Project Structure

- `Climate Folder`: Holds the Resouces folder, app.py and climate_starter.ipynb files
- `climate_starter`: The file that uses Python, SQLAlchemy ORM queries, Pandas, and Matplotlib to run the data analysis
- `app.py`: The main Flask application file that sets up the API routes and connects to the SQLite database.
- `hawaii.sqlite`: The SQLite database file containing the weather data.
  
## Part 1: Analyze and Explore the Climate Data

File: Jupyter Notebook file labeled "climate_starter"

Overview: Used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database located in the Resources file. SQLAlchemy ORM queries, Pandas, and Matplotlib were used to carry out the data analysis and visualization instrucations. 

Precipitation Analysis
- Analyze and explore the Climate Data Precipitation Analysis Finding the most recent date in the dataset, querying the previous 12 months of precipitation data then loading the query results into a Pandas DataFrame and sorting by date.

Station Analysis
- Design a query to calculate the total number of stations in the dataset and find the most-active stations, list is descending order. Query the previous 12 months of TOBS data for most active station. Plot the results as a histogram with bins=12.

## Part 2: Design Climate App

File: Python file labeled "app"

Overview: design a Flask API based on the queries in the Jupyter Notebook file labeled "climate_starter"

Available Routes and Description

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
  - This route returns the minimum, average, and maximum temperatures for a specified start date to the most recent date in JSON format.

- **Temperature Statistics for a Date Range**:
  - Go to `http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31`
  - This route returns the minimum, average, and maximum temperatures for the specified date range in JSON format.

## Resources Used
Chat GPT, Stack Overflow and previous assignments were used to help me troubleshoot problems associated with importing tables and structuring syntax appropriately.


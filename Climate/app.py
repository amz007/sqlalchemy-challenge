#Import dependencies
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Database setup
# Create an engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the existing database into a new model using automap_base()
Base = automap_base()
Base.prepare(autoload_with=engine)

# Map the classes to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session to interact with the database
session = Session(engine)

# Define the homepage route
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data."""
    # Find the most recent date in the data set
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    
    # Calculate the date one year before the most recent date
    one_year_ago = (pd.to_datetime(most_recent_date) - pd.DateOffset(years=1)).strftime('%Y-%m-%d')
    
    # Query the last 12 months of precipitation data
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()
    
    # Convert the query results to a dictionary with date as the key and prcp as the value
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    
    # Return the JSON representation of the dictionary
    return jsonify(precipitation_dict)

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    # Query all stations
    results = session.query(Station.station).all()
    
    # Convert the query results to a list
    stations_list = list(np.ravel(results))
    
    # Return the JSON list of stations
    return jsonify(stations_list)

# Define the temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature observations for the previous year for the most active station."""
    # Most active station ID
    most_active_station_id = 'USC00519281'
    
    # Find the most recent date in the data set
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    
    # Calculate the date one year before the most recent date
    one_year_ago = (pd.to_datetime(most_recent_date) - pd.DateOffset(years=1)).strftime('%Y-%m-%d')
    
    # Query the last 12 months of temperature observation data for the most active station
    temperature_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station_id).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()
    
    # Convert the query results to a list of dictionaries
    temperature_list = [{"date": date, "tobs": tobs} for date, tobs in temperature_data]
    
    # Return the JSON list of temperature observations
    return jsonify(temperature_list)

# Define the temperature range route with start date only
@app.route("/api/v1.0/<start>")
# Define the temperature range route with start and end date
@app.route("/api/v1.0/<start>/<end>")
def temp_range(start=None, end=None):
    """Return the minimum, average, and maximum temperatures for a specified date range."""
    # Define the selection of columns to query
    sel = [
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ]
    
    if not end:
        # Calculate TMIN, TAVG, TMAX for dates greater than or equal to the start date
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        # Calculate TMIN, TAVG, TMAX for dates between the start and end date inclusive
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    # Convert the query results to a list
    temps = list(np.ravel(results))
    
    # Return the JSON list of temperatures
    return jsonify({"TMIN": temps[0], "TAVG": temps[2], "TMAX": temps[1]})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

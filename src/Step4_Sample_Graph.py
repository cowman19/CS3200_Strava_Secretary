'''
This code file was used to generate the couple of visualizations of the points data
for the CS3200 Strava Secretary project.
'''

import mysql.connector
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plotMag(scale, left_x, left_y, right_x, right_y):
    fig, ax = plt.subplots()
    left_plot = ax.scatter(left_x, left_y, c=scale, cmap='plasma', marker='^', label = 'Uncalibrated', s = 10)
    fig1, ax1 = plt.subplots()
    right_plot = ax1.scatter(right_x, right_y, c=scale, cmap='plasma', label = 'Calibrated', s = 5)
    stepsize = 500
    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(start, end, stepsize))
    ax1.set_aspect('equal')
    fig.colorbar(left_plot, label='Seconds Into The Dataset', orientation = 'horizontal')#, #aspect = 100, pad = 0.01)
    fig1.colorbar(right_plot, label = 'Seconds Into The Dataset', orientation = 'horizontal', aspect = 50, pad = 0.1)
    
    ax.set_xlabel('Time and Date (Local Datetime)')
    ax.set_ylabel('Elevation (m)')
    ax.set_title('Elevation Colormapped Over Time')

    ax1.set_xlabel('Longitude (Degrees East/West)')
    ax1.set_ylabel('Latitude (Degrees North/South)')
    ax1.set_title('2D Coordinate Position Colormapped Over Time')
    ax.grid(True)
    ax1.grid(True)
    fig.tight_layout()
    fig1.tight_layout()


# Hardcoding path to the exported CSV data from the MySQL query for this one-off plot 
longest_path_df = pd.read_csv(os.path.abspath(r'C:\Users\matth\Documents\Python\CS3200\CS3200_Strava_Secretary\data\recordset.csv'))

# Converting timestamps to duration since start for good colormapping
longest_path_df['timestamp'] = pd.to_datetime(longest_path_df['time'])
start_time = longest_path_df['timestamp'].min()
longest_path_df['duration_string'] = longest_path_df['timestamp'] - start_time
longest_path_df['seconds_since_start'] = pd.to_timedelta(longest_path_df['duration_string']).dt.total_seconds()

# Extracting individual arrays from the loaded DataFrame
time = longest_path_df['seconds_since_start'].to_numpy()
elevation = longest_path_df['elevation'].to_numpy()
latitude = longest_path_df['latitude'].to_numpy()
longitude = longest_path_df['longitude'].to_numpy()

print(time)
plotMag(time, longest_path_df['time'], elevation, longitude, latitude)

# Simpler ways to plot the data we care about, but without colormapping
#longest_path_df.plot.scatter(x = 'time', y = 'elevation')
#longest_path_df.plot.scatter(x='latitude', y = 'longitude')

plt.show()
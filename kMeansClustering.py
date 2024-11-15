import pandas as pd
import numpy as np
from datetime import datetime

# Load the CSV file, ensuring the first row is treated as the header
data = pd.read_csv('attendance.csv')

# Print column names to debug
print("Columns in the DataFrame:", data.columns)

# Remove any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Validate that the 'Time' column exists
if 'Time' not in data.columns:
    raise ValueError("The 'Time' column is missing in the CSV file. Please check the header row.")

# Remove leading/trailing spaces from all values
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Validate that the 'Time' column contains valid time strings
if not data['Time'].str.match(r'^\d{2}:\d{2}:\d{2}$').all():
    invalid_times = data[~data['Time'].str.match(r'^\d{2}:\d{2}:\d{2}$')]
    print("Invalid time values found:\n", invalid_times)
    raise ValueError("The 'Time' column contains invalid time values. Please check the CSV file.")

# Function to convert time strings to minutes after midnight
def time_to_minutes(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 60 + time_obj.minute + time_obj.second / 60

# Apply the function to convert Time to Minutes
data['Minutes'] = data['Time'].apply(time_to_minutes)

# Set the college start time in minutes after midnight
college_start_time = 6 * 60 + 30  # 6:30 AM = 390 minutes

# Initialize centroids for K-Means (manual selection of early and late clusters)
early_centroid = college_start_time - 10  # Slightly before start time
late_centroid = college_start_time + 10  # Slightly after start time

# Function to calculate the distance between points and centroids
def calculate_distance(point, centroid):
    return abs(point - centroid)

# K-Means Clustering loop
max_iterations = 100
for _ in range(max_iterations):
    # Assign students to the nearest cluster
    data['Cluster'] = data['Minutes'].apply(
        lambda x: 0 if calculate_distance(x, early_centroid) < calculate_distance(x, late_centroid) else 1
    )
    
    # Calculate new centroids
    new_early_centroid = data[data['Cluster'] == 0]['Minutes'].mean()
    new_late_centroid = data[data['Cluster'] == 1]['Minutes'].mean()
    
    # Check for convergence (if centroids don't change)
    if np.isclose(new_early_centroid, early_centroid) and np.isclose(new_late_centroid, late_centroid):
        break
    
    # Update centroids
    early_centroid = new_early_centroid
    late_centroid = new_late_centroid

# Assign human-readable categories
data['Category'] = data['Cluster'].apply(
    lambda cluster: 'Early Arrival' if cluster == 0 else 'Late Arrival'
)

# Save or display categorized data
print(data[['Name', 'Minutes', 'Category']])

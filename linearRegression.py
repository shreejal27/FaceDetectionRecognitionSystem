import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = pd.read_csv('attendance.csv', header=None, names=['ID', 'UserID', 'Name', 'Faculty', 'Time', 'Date', 'Status'])

data['Name'] = data['Name'].str.strip().str.lower()
data['Faculty'] = data['Faculty'].str.strip().str.lower()
data['Time'] = data['Time'].str.strip()  # Remove leading/trailing spaces

filtered_data = data[(data['Name'] == 'hari') & (data['Faculty'] == 'bsc')]

if filtered_data.empty:
    print("No matching records found for the given filters.")
    raise ValueError("Filtered data is empty. Please check the filtering conditions.")

def time_to_minutes(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 60 + time_obj.minute + time_obj.second / 60

filtered_data['Minutes'] = filtered_data['Time'].apply(time_to_minutes)

# Prepare X and Y for linear regression
X = np.arange(len(filtered_data)) + 1  # Days as 1, 2, 3, ...
Y = filtered_data['Minutes'].values    # Arrival times in minutes

# Validate non-zero data for regression
if len(X) < 2 or len(Y) < 2:
    raise ValueError("Not enough data points for linear regression.")

X_mean = X.mean()
Y_mean = Y.mean()
denominator = np.sum((X - X_mean) ** 2)
if denominator == 0:
    raise ValueError("Variance in X is zero; cannot perform linear regression.")

m = np.sum((X - X_mean) * (Y - Y_mean)) / denominator
b = Y_mean - m * X_mean

# Predict arrival time for the next day
next_day = len(X) + 1
predicted_minutes = m * next_day + b

# Convert predicted minutes back to HH:MM:SS format
predicted_time = (datetime.strptime("00:00:00", "%H:%M:%S") + timedelta(minutes=predicted_minutes)).strftime("%H:%M:%S")

print(f"Predicted arrival time for the next day: {predicted_time}")

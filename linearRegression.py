import numpy as np
from datetime import timedelta, datetime

# Sample data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
Y = np.array([10, 12, 11, 9, 13, 15, 8, 14, 10, 12, 9, 13, 15, 8, 10])

# Calculate the means of X and Y
X_mean = np.mean(X)
Y_mean = np.mean(Y)

# Calculate the slope (m) and intercept (b)
numerator = np.sum((X - X_mean) * (Y - Y_mean))
denominator = np.sum((X - X_mean) ** 2)
m = numerator / denominator
b = Y_mean - m * X_mean

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict function
def predict(day):
    return m * day + b

# Predict arrival time for day 16
predicted_time_day_16 = predict(16)
print(f"Predicted arrival time on day 16 (minutes after 6:30): {predicted_time_day_16:.2f}")

base_time = datetime.strptime("6:30 AM", "%I:%M %p")

# Predict arrival time for day 16 in minutes after 6:30 AM
predicted_minutes_day_16 = predict(16)

# Add the predicted minutes to the base time
predicted_time_formatted = (base_time + timedelta(minutes=predicted_minutes_day_16)).strftime("%I:%M %p")

print(f"Predicted arrival time on day 16: {predicted_time_formatted}")

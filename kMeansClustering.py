import numpy as np
import pandas as pd
from datetime import datetime

# Sample Data
data = [
    {"ID": 1, "UserID": 1, "Name": "shyam", "Faculty": "BCA", "Time": "06:23:02", "Date": "01/10/2024", "Status": "Present"},
    {"ID": 4, "UserID": 1, "Name": "shyam", "Faculty": "BCA", "Time": "06:35:05", "Date": "02/10/2024", "Status": "Present"},
    {"ID": 7, "UserID": 1, "Name": "shyam", "Faculty": "BCA", "Time": "06:36:15", "Date": "03/10/2024", "Status": "Present"},
    {"ID": 10, "UserID": 1, "Name": "shyam", "Faculty": "BCA", "Time": "06:34:00", "Date": "04/10/2024", "Status": "Present"},
    # Add more rows for shyam as needed
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Function to convert time to seconds
def time_to_seconds(time_str):
    t = datetime.strptime(time_str, "%H:%M:%S")
    return t.hour * 3600 + t.minute * 60 + t.second

# Filter data for a specific student
user_id = 1  # Input from user
student_data = df[df['UserID'] == user_id]
arrival_times = student_data['Time'].apply(time_to_seconds).values

# K-Means Clustering Implementation
def k_means_clustering(data, k=3, max_iter=100):
    # Randomly initialize centroids
    centroids = np.random.choice(data, k, replace=False)
    for _ in range(max_iter):
        # Assign clusters
        clusters = {i: [] for i in range(k)}
        for point in data:
            distances = [abs(point - centroid) for centroid in centroids]
            cluster = distances.index(min(distances))
            clusters[cluster].append(point)
        
        # Update centroids
        new_centroids = np.array([np.mean(clusters[i]) if clusters[i] else centroids[i] for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return clusters, centroids

# Apply K-Means
k = 3  # Number of clusters
clusters, centroids = k_means_clustering(arrival_times, k)

# Print Results
print("Clusters:")
for cluster_id, points in clusters.items():
    print(f"Cluster {cluster_id + 1}: {points}")

print("\nCentroids (in seconds):", centroids)

# Optional: Convert centroids back to time format
def seconds_to_time(seconds):
    return str(datetime.utcfromtimestamp(seconds).time())

print("\nCentroids (in HH:MM:SS):", [seconds_to_time(c) for c in centroids])

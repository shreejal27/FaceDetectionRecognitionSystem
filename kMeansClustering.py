from tkinter import *
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd
from datetime import datetime

class KMeansClusteringWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Behavior Analysis with K-Means")
        self.root.geometry("750x550")

        # Frame for inputs
        input_frame = Frame(self.root, bd=2, relief=RIDGE, padx=10, pady=10)
        input_frame.place(x=50, y=50, width=650, height=200)

        title = Label(input_frame, text="K-Means Clustering - Arrival Time Analysis", font=("Arial", 16, "bold"))
        title.grid(row=0, columnspan=2, pady=10)

        # Name Input
        lbl_name = Label(input_frame, text="Name:", font=("Arial", 12))
        lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.entry_name = Entry(input_frame, font=("Arial", 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        # Faculty Input
        lbl_faculty = Label(input_frame, text="Faculty:", font=("Arial", 12))
        lbl_faculty.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.entry_faculty = Entry(input_frame, font=("Arial", 12))
        self.entry_faculty.grid(row=2, column=1, padx=10, pady=5)

        # Number of Clusters Input
        lbl_clusters = Label(input_frame, text="Number of Clusters (k):", font=("Arial", 12))
        lbl_clusters.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.entry_clusters = Entry(input_frame, font=("Arial", 12))
        self.entry_clusters.grid(row=3, column=1, padx=10, pady=5)

        # Predict Button
        btn_predict = Button(input_frame, text="Analyze Behavior", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.run_kmeans)
        btn_predict.grid(row=4, columnspan=2, pady=10)

        # Frame for Output
        self.output_frame = Frame(self.root, bd=2, relief=RIDGE, padx=10, pady=10)
        self.output_frame.place(x=50, y=300, width=650, height=200)

        lbl_output = Label(self.output_frame, text="Results:", font=("Arial", 14, "bold"))
        lbl_output.grid(row=0, column=0, sticky=W)

        # Scrollbar and Text for results
        self.scrollbar = Scrollbar(self.output_frame, orient=VERTICAL)
        self.scrollbar.grid(row=1, column=1, sticky=NS)

        self.output_label = Text(self.output_frame, wrap=WORD, font=("Arial", 12), bg="lightgrey", state=DISABLED, yscrollcommand=self.scrollbar.set)
        self.output_label.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

        self.scrollbar.config(command=self.output_label.yview)

        self.output_frame.grid_rowconfigure(1, weight=1)
        self.output_frame.grid_columnconfigure(0, weight=1)

    def run_kmeans(self):
        try:
            # Validate inputs
            name = self.entry_name.get().strip().lower()
            faculty = self.entry_faculty.get().strip().lower()
            k_clusters = self.entry_clusters.get().strip()

            if not name or not faculty or not k_clusters:
                raise ValueError("Name, Faculty, and Number of Clusters are required.")
            
            k_clusters = int(k_clusters)
            if k_clusters < 1:
                raise ValueError("Number of clusters (k) must be at least 1.")

            # Read data from CSV
            try:
                data = pd.read_csv("attendance.csv", header=None, names=['ID', 'UserID', 'Name', 'Faculty', 'Time', 'Date', 'Status'])
            except FileNotFoundError:
                raise ValueError("File 'attendance.csv' not found. Please ensure the file exists.")

            # Preprocess data
            data['Name'] = data['Name'].str.strip().str.lower()
            data['Faculty'] = data['Faculty'].str.strip().str.lower()
            data['Time'] = data['Time'].str.strip()

            # Filter data for the specific student
            student_data = data[(data['Name'] == name) & (data['Faculty'] == faculty)]
            if student_data.empty:
                raise ValueError(f"No data found for Name '{name}' in Faculty '{faculty}'.")

            # Function to convert time to seconds
            def time_to_seconds(time_str):
                t = datetime.strptime(time_str, "%H:%M:%S")
                return t.hour * 3600 + t.minute * 60 + t.second

            arrival_times = student_data['Time'].apply(time_to_seconds).values

            # K-Means Clustering Implementation
            def k_means_clustering(data, k=3, max_iter=100):
                centroids = np.random.choice(data, k, replace=False)
                for _ in range(max_iter):
                    clusters = {i: [] for i in range(k)}
                    for point in data:
                        distances = [abs(point - centroid) for centroid in centroids]
                        cluster = distances.index(min(distances))
                        clusters[cluster].append(point)
                    
                    new_centroids = np.array([np.mean(clusters[i]) if clusters[i] else centroids[i] for i in range(k)])
                    if np.all(centroids == new_centroids):
                        break
                    centroids = new_centroids
                
                return clusters, centroids

            # Apply K-Means
            clusters, centroids = k_means_clustering(arrival_times, k_clusters)

            # Convert centroids back to time format
            def seconds_to_time(seconds):
                return str(datetime.utcfromtimestamp(seconds).time())

            # Display results
            results = []
            for cluster_id, points in clusters.items():
                cluster_time = [seconds_to_time(p) for p in points]
                cluster_total = len(points)
                results.append(f"Cluster {cluster_id + 1}: {', '.join(cluster_time)} \n Total: {cluster_total} \n")
            
            results.append("\nCentroids (in HH:MM:SS):")
            for cluster_id, centroid in enumerate(centroids):
                results.append(f"Cluster {cluster_id + 1}: Centroid: {seconds_to_time(centroid)}")

            self.output_label.config(state=NORMAL)
            self.output_label.delete(1.0, END)
            self.output_label.insert(END, "\n".join(results))
            self.output_label.config(state=DISABLED)

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Driver code
if __name__ == "__main__":
    root = Tk()
    app = KMeansClusteringWindow(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class LinearRegressionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Arrival Time Predictor")
        self.root.geometry("600x400")

        # Frame for inputs
        input_frame = Frame(self.root, bd=2, relief=RIDGE, padx=10, pady=10)
        input_frame.place(x=50, y=50, width=500, height=200)

        title = Label(input_frame, text="Predict Arrival Time", font=("Arial", 16, "bold"))
        title.grid(row=0, columnspan=2, pady=10)

        # Name Input
        lbl_name = Label(input_frame, text="Student Name:", font=("Arial", 12))
        lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.entry_name = Entry(input_frame, font=("Arial", 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        # Faculty Input
        lbl_faculty = Label(input_frame, text="Faculty:", font=("Arial", 12))
        lbl_faculty.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.entry_faculty = Entry(input_frame, font=("Arial", 12))
        self.entry_faculty.grid(row=2, column=1, padx=10, pady=5)

        # Predict Button
        btn_predict = Button(input_frame, text="Predict Arrival Time", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.predict_time)
        btn_predict.grid(row=3, columnspan=2, pady=10)

        # Frame for Output
        self.output_frame = Frame(self.root, bd=2, relief=RIDGE, padx=10, pady=10)
        self.output_frame.place(x=50, y=270, width=500, height=100)

        lbl_output = Label(self.output_frame, text="Predicted Arrival Time:", font=("Arial", 14, "bold"))
        lbl_output.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.output_label = Label(self.output_frame, text="", font=("Arial", 14), fg="green")
        self.output_label.grid(row=0, column=1, padx=10, pady=5)

    def predict_time(self):
        try:
            # Get inputs from user
            name = self.entry_name.get().strip().lower()
            faculty = self.entry_faculty.get().strip().lower()

            if not name or not faculty:
                raise ValueError("Both Name and Faculty are required.")

            # Load and filter data
            data = pd.read_csv('attendance.csv', header=None, names=['ID', 'UserID', 'Name', 'Faculty', 'Time', 'Date', 'Status'])
            data['Name'] = data['Name'].str.strip().str.lower()
            data['Faculty'] = data['Faculty'].str.strip().str.lower()
            data['Time'] = data['Time'].str.strip()

            filtered_data = data[(data['Name'] == name) & (data['Faculty'] == faculty)]

            if filtered_data.empty:
                raise ValueError("No matching records found for the given filters.")

            # Convert time to minutes
            def time_to_minutes(time_str):
                time_obj = datetime.strptime(time_str, "%H:%M:%S")
                return time_obj.hour * 60 + time_obj.minute + time_obj.second / 60

            filtered_data['Minutes'] = filtered_data['Time'].apply(time_to_minutes)

            # Prepare data for regression
            X = np.arange(len(filtered_data)) + 1
            Y = filtered_data['Minutes'].values

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
            predicted_time = (datetime.strptime("00:00:00", "%H:%M:%S") + timedelta(minutes=predicted_minutes)).strftime("%H:%M:%S")

            # Display predicted time
            self.output_label.config(text=predicted_time)

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Driver code
if __name__ == "__main__":
    root = Tk()
    app = LinearRegressionWindow(root)
    root.mainloop()

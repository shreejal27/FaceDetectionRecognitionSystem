from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from linearRegression import LinearRegressionWindow
from kMeansClustering import KMeansClusteringWindow


class Predict:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        b1_1 = Button(self.root, text="Student Arrival Estimator", cursor="hand2", command=self.linearRegressionWindow, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=400, width=500, height=50)

        b1_2 = Button(self.root, text="Student Arrival Patterns ", cursor="hand2", command=self.kMeansClusteringWindow, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_2.place(x=1000, y=400, width=500, height=50)

    #Functions button
    def linearRegressionWindow(self):
        self.new_window = Toplevel(self.root)
        self.app = LinearRegressionWindow(self.new_window)
    
    def kMeansClusteringWindow(self):
        self.new_window = Toplevel(self.root)
        self.app = KMeansClusteringWindow(self.new_window)

if __name__ == "__main__":
    root = Tk() 
    obj = Predict(root)
    root.mainloop()

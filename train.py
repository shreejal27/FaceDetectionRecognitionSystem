from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:

    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="Train Data",  font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        
        b1_1 = Button(self.root, text="Train the data!",command=self.train_classifer, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=400, width=1530, height=50 )

    
    def train_classifer(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img= Image.open(image).convert('L') #to convert image to grayscale

            imageNp=np.array(img, 'uint8') #converting image to numpy array (grid)

            id=int(os.path.split(image)[1].split('.')[1]) 

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids=np.array(ids)



        #Train the classifier and save
        
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!!!")







if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Train(root)
    root.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
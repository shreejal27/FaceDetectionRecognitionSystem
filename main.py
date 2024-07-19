from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing


class Face_Recognition_System:

    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)



        #student button
        img1 = Image.open(r"Images\students.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(self.root, image=self.photoimg1, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)



        #Detect Face button
        img2 = Image.open(r"Images\students.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(self.root, image=self.photoimg2, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)



        #Attendance Button
        img3 = Image.open(r"Images\students.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(self.root, image=self.photoimg3, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(self.root, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)



        #Train Face Button
        img4 = Image.open(r"Images\students.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=400, width=220, height=220)

        b1_1 = Button(self.root, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=600, width=220, height=40 )



       #Photos Button
        img5 = Image.open(r"Images\students.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(self.root, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(self.root, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=600, width=220, height=40 )



       #Exit Button
        img6 = Image.open(r"Images\students.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(self.root, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_1 = Button(self.root, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=600, width=220, height=40 )






if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Face_Recognition_System(root)
    root.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
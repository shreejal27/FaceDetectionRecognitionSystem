from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing


class Face_Recognition_System:
    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Face_Recognition_System(root)
    root.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
from time import strftime
from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing
from tkinter import messagebox
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:

    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="Face Recognition",  font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=400, width=1530, height=50 )


    #attendance
    def mark_attendance(self, i, r, n, d):
        with open("Attendance.csv", "r+", newline="\n") as file:
            myDataList = file.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                file.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1} ,  Present")
      
    # Face Recognition

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coords = []

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), color ,3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence= int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n=my_cursor.fetchone()
                n="+".join(n) if n else "Unknown"

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r=my_cursor.fetchone()
                r="+".join(r) if r else "Unknown"

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d=my_cursor.fetchone()
                d="+".join(d) if d else "Unknown"

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i=my_cursor.fetchone()
                i="+".join(i) if i else "Unknown"



                if confidence > 77:
                    cv2.putText(img,f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0, 255),3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                
                #coord=[x,y,w,y]
                coords.append((x, y, w, h))  # Collect coordinates
                
            return coords
        

        def recognize(img, clf, faceCascade):
            coord= draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) ==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Face_Recognition(root)
    root.mainloop()
    
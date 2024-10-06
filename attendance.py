from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:

    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Attendance Management", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=700)

        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=550)

        
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=15, width=720, height=450)

        #Label entry 
        #Attendance ID
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"),bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #Roll 
        rollLabel = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"),bg="white")
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        attendance_roll = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendance_roll.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #Name 
        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"),bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        attendance_name = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendance_name.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        #Department 
        depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"),bg="white")
        depLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        attendance_dep = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendance_dep.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Time 
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"),bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        attendance_time = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendance_time.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #Date 
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"),bg="white")
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        attendance_date = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendance_date.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #Attendance 
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"),bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 13, "bold"), state="readonly")
        self.atten_status["values"] = ("Select", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)


        #Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=220, width=680, height=40)

        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        delete_btn = Button(btn_frame, text="Export CSV", command= self.exportCsv, width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=550)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=15, width=720, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

    
    #fetch data

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfile(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("All Files", "*.*")), parent=self.root)
        with open(fln.name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",defaultextension=".csv", filetypes=(("CSV File", "*.csv"),("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write= csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)






if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Attendance(root)
    root.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
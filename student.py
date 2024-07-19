from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing


class Student:

    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Student Management System", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=700)

        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=650)

        #Current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=10, y=30, width=700, height=120)


        #Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "BCA", "Bsc.CSIT", "BBM", "BBA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)



        #Year
        course_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=1, column=0, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)



        #Semester
        course_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=1, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)



        #Class Student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=10, y=170, width=700, height=450)


        #Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #Student Name 
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"),bg="white")
        #studentName_label.grid(row=0, column=2, padx=10, sticky=W)
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #Class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        class_div_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        #Roll No
        rollNo_label = Label(class_student_frame, text="Roll No: ", font=("times new roman", 13, "bold"),bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        rollNo_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        
        #Gender
        gender_label = Label(class_student_frame, text="Gender: ", font=("times new roman", 13, "bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)



        #DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        #Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"),bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        #Phone
        phone_label = Label(class_student_frame, text="Phone:", font=("times new roman", 13, "bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        
        #Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        #Teacher
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(class_student_frame, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)



        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=650)



if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Student(root)
    root.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
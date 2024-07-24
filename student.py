from tkinter import * # for making powerful GUI model
from tkinter import ttk  
from PIL import Image, ImageTk # for image cropping and resizing
from tkinter import messagebox
import mysql.connector

class Student:

    def __init__(self, root): # constructor
        self.root = root # root is the main window ; initializing the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #Variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



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

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "BCA", "Bsc.CSIT", "BBM", "BBA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)



        #Year
        course_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=1, column=0, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)



        #Semester
        course_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=1, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)



        #Class Student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=10, y=170, width=700, height=450)


        #Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #Student Name 
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"),bg="white")
        #studentName_label.grid(row=0, column=2, padx=10, sticky=W)
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #Class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), width=18, state="readonly")
        div_combo["values"] = ("", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        #Roll No
        rollNo_label = Label(class_student_frame, text="Roll No: ", font=("times new roman", 13, "bold"),bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        rollNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        
        #Gender
        gender_label = Label(class_student_frame, text="Gender: ", font=("times new roman", 13, "bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
           
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)




        #DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        #Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"),bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        #Phone
        phone_label = Label(class_student_frame, text="Phone:", font=("times new roman", 13, "bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        
        #Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        #Teacher
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)



        #Radio Buttons
        self.var_radio1= StringVar()
        radiobtn1= ttk.Radiobutton(class_student_frame, variable=self.var_radio1,  text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2= ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)


        #Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=220, width=680, height=40)

        save_btn = Button(btn_frame, text="Save", command=self.add_data,  width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        #Buttons Frame
        btn_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=10, y=260, width=680, height=40)

        take_photo_btn = Button(btn_frame2, text="Take Photo Sample",width=33, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame2, text="Update Photo Sample",width=33, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)






        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=650)


        #Search System
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=10, y=20, width=700, height=100)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"),bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll_No", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)


        search_btn = Button(search_frame, text="Search",width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=5, pady=5, sticky=W)

        showAll_btn = Button(search_frame, text="Show All",width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4,padx=5, pady=5, sticky=W)



        
        #Table Frame
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=130, width=700, height=500)


        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)    
        self.student_table.column("course", width=100)    
        self.student_table.column("year", width=100)    
        self.student_table.column("sem", width=100)    
        self.student_table.column("id", width=100)    
        self.student_table.column("name", width=100)    
        self.student_table.column("div", width=100)    
        self.student_table.column("roll", width=100)    
        self.student_table.column("gender", width=100)    
        self.student_table.column("dob", width=100)    
        self.student_table.column("email", width=100)    
        self.student_table.column("phone", width=100)    
        self.student_table.column("address", width=100)    
        self.student_table.column("teacher", width=100)    
        self.student_table.column("photo", width=150)    

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #Function decleration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_dep.get(),
                                                                                self.var_course.get(),
                                                                                self.var_year.get(),
                                                                                self.var_semester.get(),
                                                                                self.var_std_id.get(),
                                                                                self.var_std_name.get(),
                                                                                self.var_div.get(),
                                                                                self.var_roll.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phone.get(),
                                                                                self.var_address.get(),
                                                                                self.var_teacher.get(),
                                                                                self.var_radio1.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
                

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data= my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()    
        content = self.student_table.item(cursor_focus) 
        data = content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    

    #Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student  SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",(
                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_std_name.get(),
                                                                    self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_address.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_std_id.get(),
                                    ))
                else:
                    if not Update:
                        return 

                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)                           
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)


    #Delete Function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()

                    sql="delete from student where Student_id = %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return  
                
                conn.commit()
                self.fetch_data()
                conn.close()          
                messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)
            
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set("Select Department"),
        self.var_std_name.set("Select Department"),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        
            








if __name__ == "__main__":
    root = Tk() # creating the object of the class
    obj = Student(root)
    root.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
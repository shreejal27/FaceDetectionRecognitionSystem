from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=600, y=200, width=400, height=500)

        register_label = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), bg="black", fg="white")
        register_label.place(x=120, y=50)

     # Name
        name_label = Label(frame, text="Name", font=("times new roman", 15, "bold"), bg="black", fg="white")
        name_label.place(x=50, y=120)
        self.txt_name = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_name.place(x=50, y=150, width=250)

        # Username
        username_label = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username_label.place(x=50, y=190)
        self.txt_username = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_username.place(x=50, y=220, width=250)

        # Password
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password_label.place(x=50, y=260)
        self.txt_password = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txt_password.place(x=50, y=290, width=250)

        # Confirm Password
        confirm_password_label = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        confirm_password_label.place(x=50, y=330)
        self.txt_confirm_password = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txt_confirm_password.place(x=50, y=360, width=250)

        # Register button
        registerbtn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="black", fg="white")
        registerbtn.place(x=50, y=420, width=250)

    def register_data(self):
        if self.txt_name.get() == "" or self.txt_username.get() == "" or self.txt_password.get() == "" or self.txt_confirm_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_confirm_password.get():
            messagebox.showerror("Error", "Password and Confirm Password should be same", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="", 
                    database="face_recognizer"
                )
                cursor = conn.cursor()

                # Check if the student exists in the 'student' table
                cursor.execute("SELECT * FROM student WHERE name = %s", (self.txt_name.get(),))
                student_record = cursor.fetchone()

                if student_record is None:
                    messagebox.showerror("Error", "Registration Faild! You are not recorded in the system", parent=self.root)
                
                else:
                # Insert query to store registration data
                    cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", 
                                (self.txt_username.get(), self.txt_password.get()))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Register_Window(root)
    root.mainloop()
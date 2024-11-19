from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from main import Face_Recognition_System
from register import Register_Window
from face_recognition import Face_Recognition
import mysql.connector

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1550x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=600, y=200, width=350, height= 450)

        get_str = Label(frame, text= "Get Started", font=("times new roman", 20, "bold"), bg="black", fg="white")
        get_str.place(x=100, y=70)

        #label
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username.place(x=50, y=150)
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password.place(x=50, y=220)

        #entry
        self.txt_username = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_username.place(x=50, y=180, width=250)
        self.txt_password = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txt_password.place(x=50, y=250, width=250)

        #Loginbutton
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="black", fg="white")    
        loginbtn.place(x=50, y=300, width=250)

        #Registerbutton
        registerbtn = Button(frame, text="Register", command=self.register, font=("times new roman", 15, "bold"), borderwidth=0, bg="black", fg="white")    
        registerbtn.place(x=50, y=370, width=100)

        #Forgot Password
        forgotbtn = Button(frame, text="Forgot Password", font=("times new roman", 15, "bold"), borderwidth=0, bg="black", fg="white")    
        forgotbtn.place(x=160, y=370, width=150)

    def login(self):

        username = self.txt_username.get()
        password = self.txt_password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",      
                    user="root",    
                    password="",  
                    database="face_recognizer"    
                )

                cursor = connection.cursor()
                query = "SELECT * FROM login WHERE username=%s AND password=%s "
                cursor.execute(query, (username, password))
                result = cursor.fetchone()
                
                if result:
                    usertype = result[3]

                    if usertype == "admin":
                        messagebox.showinfo("Success", "Welcome Admin", parent=self.root)
                        self.root.withdraw() 
                        self.show_main() 
                    
                    elif usertype == 'student':
                        messagebox.showinfo("Success", "Welcome to Face Detection and Recognition", parent=self.root)
                        self.root.withdraw() 
                        self.show_face_recognition()  
                else:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)

                connection.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_Window(self.new_window)
    
    def show_face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    
    def show_main(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)

        #variables
        self.var_username = StringVar()
        self.var_password = StringVar()

        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="white", fg="blue")
        title.place(x=0, y=0, relwidth=1)




if __name__ == "__main__":
    root = Tk()
    app =  Login_Window(root)
    root.mainloop()

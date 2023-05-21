
import tkinter as tk
from tkinter import ttk
from tkinter import Label, PhotoImage, ttk


class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Data Base Management System")
        self.window.geometry("1100x600")  # Set the initial size of the window
        # self.window.configure(bg= "#fafafa")
        self.bg = PhotoImage(file = "bg.png")
        self.label1 = Label(self.window, image = self.bg)
        self.label1.place(x = 0, y = 0)


        self.style = ttk.Style()
        self.style.configure('TLabel', background='white', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))


        self.login_frame = ttk.Frame(self.window, padding=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        LoginScreen(self.window, self.login_frame)


    def start(self):
        self.window.mainloop()




class LoginScreen():
    def __init__(self, window, frame):
        self.window = window
        self.frame = frame

        # Add logo
        # self.login_logo = tk.PhotoImage(file="book.png")
        # self.logo_label = ttk.Label(self.frame, image=self.login_logo)
        # self.logo_label.grid(row=0, column=0, columnspan=2)

        # Add login widgets
        self.login_email_label = ttk.Label(self.frame, text="Email:")
        self.login_email_label.grid(row=1, column=0, sticky="e")
        self.login_email_entry = ttk.Entry(self.frame)
        self.login_email_entry.grid(row=1, column=1)

        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=2, column=0, sticky="e")
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1)

        self.login_button = ttk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, sticky="e")

        self.signup_link = ttk.Label(self.frame, text="Don't have an account? ", cursor="hand2")
        self.signup_link.grid(row=4, column=0, sticky="e")
        self.signup_button = ttk.Button(self.frame, text="Signup", command=self.show_signup_frame)
        self.signup_button.grid(row=4, column=1, sticky="w")
        # self.signup_link = ttk.Label(self.frame, text="Don't have an account? Sign up!", cursor="hand2")
        # self.signup_link.pack()
        # self.signup_link.bind("<Button-1>", lambda event: self.show_signup_frame)

    def login(self):
        # Retrieve entered username and password
        username = self.login_email_entry.get()
        password = self.password_entry.get()

        # Placeholder validation logic
        if username == "admin" and password == "password":
            # Successful login
            print("Login successful!")
            self.show_home_frame()
            # main.show_main_frame()
        else:
            # Invalid login
            print("Invalid username or password")

    def show_signup_frame(self):
        # Hide the login frame
        print("show signup frame")
        self.frame.place_forget()
        # Show the signup frame
        self.signup_frame = ttk.Frame(self.window, padding=20)
        self.signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        SignupScreen(self.window, self.signup_frame)

    def show_home_frame(self):
        # Hide the login frame
        self.frame.place_forget()
        # Show the home frame
        self.home_frame = ttk.Frame(self.window, padding=20)
        self.home_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        HomeScreen(self.window, self.home_frame)



class SignupScreen:
    def __init__(self,window,frame):
        self.window = window
        self.frame = frame
        # self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add signup widgets
        self.first_name_label = ttk.Label(self.frame, text="First Name:")
        self.first_name_label.pack()
        self.first_name_entry = ttk.Entry(self.frame)
        self.first_name_entry.pack()

        self.last_name_label = ttk.Label(self.frame, text="Last Name:")
        self.last_name_label.pack()
        self.last_name_entry = ttk.Entry(self.frame)
        self.last_name_entry.pack()

        self.signup_email_label = ttk.Label(self.frame, text="Email:")
        self.signup_email_label.pack()
        self.signup_email_entry = ttk.Entry(self.frame)
        self.signup_email_entry.pack()

        self.new_password_label = ttk.Label(self.frame, text="New Password:")
        self.new_password_label.pack()
        self.new_password_entry = ttk.Entry(self.frame, show="*")
        self.new_password_entry.pack()

        self.confirm_password_label = ttk.Label(self.frame, text="Confirm Password:")
        self.confirm_password_label.pack()
        self.confirm_password_entry = ttk.Entry(self.frame, show="*")
        self.confirm_password_entry.pack()

        self.signup_button = ttk.Button(self.frame, text="Sign Up", command=self.signup)
        self.signup_button.pack()

        self.signup_link = ttk.Label(self.frame, text="Already have an account? ")
        self.signup_link.pack()
        self.signup_button = ttk.Button(self.frame, text="Login!", command=self.show_login_frame)  
        self.signup_button.pack()

        # self.login_link = ttk.Label(self.frame, text="Already have an account? Login!", cursor="hand2")
        # self.login_link.pack()
        # self.login_link.bind("<Button-1>", lambda event: self.show_login_frame)

    def signup(self):
        # Retrieve entered details from signup fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.signup_email_entry.get()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Placeholder signup logic
        if password == confirm_password and len(password) >= 1:
            # Successful signup
            print("Signup successful!")
            print(f"Name: {first_name} {last_name}")
            print(f"Email: {email}")
            # login.show_login_frame()
            # signup_frame.place_forget()
        else:
            # Passwords do not match
            print("Passwords do not match")

    def show_login_frame(self):
        # Hide the signup frame

        self.frame.place_forget()
        self.login_frame = ttk.Frame(self.window, padding=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        LoginScreen(self.window, self.login_frame)
        # Show the login frame
        # self.login_frame = ttk.Frame(self.window, padding=20)
        # self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # LoginScreen(self.window, self.login_frame)


class HomeScreen:
    def __init__(self, window, frame):
        self.window = window
        self.frame = frame

        self.home_label = ttk.Label(self.frame, text="Home Screen")
        self.home_label.pack()
        # Create a navigation bar frame
        self.nav_frame = ttk.Frame(self.frame)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)
        self.nav_frame.config(padding=(0, 5))
        # self.nav_frame.grid(row=0, column=0)

        # Add buttons to the navigation bar
        self.edit_profile_button = ttk.Button(self.nav_frame, text="", command=self.edit_profile)
        # self.edit_profile_button.pack(side=tk.LEFT)
        img = tk.PhotoImage(file="button.png") # make sure to add "/" not "\"
        self.edit_profile_button.config(image=img)
        self.edit_profile_button.grid(row=0, column=0)

        self.logout_button = ttk.Button(self.nav_frame, text="Logout", command=self.logout)
        # self.logout_button.pack(side=tk.LEFT)
        self.logout_button.grid(row=0, column=1)

        self.browse_books_button = ttk.Button(self.nav_frame, text="Browse Books", command=self.browse_books)
        # self.browse_books_button.pack(side=tk.LEFT)
        self.browse_books_button.grid(row=0, column=2)


    def logout(self):
        # Hide the home frame
        self.frame.place_forget()
        # Show the login frame
        self.login_frame = ttk.Frame(self.window, padding=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        LoginScreen(self.window, self.login_frame)

    def edit_profile(self):
        # Handle the "Edit Profile" button click event
        # Add your code to open the edit profile screen or perform any related action
        pass

    def browse_books(self):
        # Handle the "Browse Books" button click event
        # Add your code to open the browse books screen or perform any related action
        pass


MyGUI().start()
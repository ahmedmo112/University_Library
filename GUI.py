import tkinter as tk

def show_login_frame():
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    signup_frame.place_forget()

def show_signup_frame():
    signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    login_frame.place_forget()

# Function to perform login
def login():
    # Retrieve entered username and password
    username = login_email_entry.get()
    password = password_entry.get()

    # Placeholder validation logic
    if username == "admin" and password == "password":
        # Successful login
        print("Login successful!")
    else:
        # Invalid login
        print("Invalid username or password")

# Function to perform signup
def signup():
    # Retrieve entered details from signup fields
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = signup_email_entry.get()
    password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Placeholder signup logic
    if password == confirm_password:
        # Successful signup
        print("Signup successful!")
        print(f"Name: {first_name} {last_name}")
        print(f"Email: {email}")
    else:
        # Passwords do not match
        print("Passwords do not match")

# Create the main window
window = tk.Tk()
window.title("Data Base Management System")
window.geometry("1100x600")  # Set the initial size of the window
window.configure(bg='lightgray')

# Create the login frame
login_frame = tk.Frame(window, bg='lightgray')
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add login widgets
login_email_label = tk.Label(login_frame, text="Email:")
login_email_label.pack()
login_email_entry = tk.Entry(login_frame)
login_email_entry.pack()

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

signup_link = tk.Label(login_frame, text="Don't have an account? Sign up!", fg="blue", cursor="hand2")
signup_link.pack()
signup_link.bind("<Button-1>", lambda event: show_signup_frame())

# Create the signup frame
signup_frame = tk.Frame(window, bg='lightgray')
signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
signup_frame.place_forget()  # Initially hide the signup frame

# Add signup widgets
first_name_label = tk.Label(signup_frame, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(signup_frame)
first_name_entry.pack()

last_name_label = tk.Label(signup_frame, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(signup_frame)
last_name_entry.pack()

signup_email_label = tk.Label(signup_frame, text="Email:")
signup_email_label.pack()
signup_email_entry = tk.Entry(signup_frame)
signup_email_entry.pack()

new_password_label = tk.Label(signup_frame, text="New Password:")
new_password_label.pack()
new_password_entry = tk.Entry(signup_frame, show="*")
new_password_entry.pack()

confirm_password_label = tk.Label(signup_frame, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(signup_frame, show="*")
confirm_password_entry.pack()

signup_button = tk.Button(signup_frame, text="Sign Up", command=signup)
signup_button.pack()

login_link = tk.Label(signup_frame, text="Already have an account? Login!", fg="blue", cursor="hand2")
login_link.pack()
login_link.bind("<Button-1>", lambda event: show_login_frame())

# Raise the login frame initially
show_login_frame()

window.mainloop()



# # from main import signup_frame , window ,show_main_frame,show_signup_frame , ttk , tk


# import tkinter as tk
# from tkinter import ttk
# from main_functions import show_main_frame, show_signup_frame
# from main import window

# def show_login_frame():
#     login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#     signup_frame.place_forget()


# def login():
#     # Retrieve entered username and password
#     username = login_email_entry.get()
#     password = password_entry.get()

#     # Placeholder validation logic
#     if username == "admin" and password == "password":
#         # Successful login
#         print("Login successful!")
#         show_main_frame()
#     else:
#         # Invalid login
#         print("Invalid username or password")


# # Create the login frame
# login_frame = ttk.Frame(window, padding=20)
# login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# # Add login widgets
# login_email_label = ttk.Label(login_frame, text="Email:")
# login_email_label.pack()
# login_email_entry = ttk.Entry(login_frame)
# login_email_entry.pack()

# password_label = ttk.Label(login_frame, text="Password:")
# password_label.pack()
# password_entry = ttk.Entry(login_frame, show="*")
# password_entry.pack()

# login_button = ttk.Button(login_frame, text="Login", command=login)
# login_button.pack()

# signup_link = ttk.Label(login_frame, text="Don't have an account? Sign up!", cursor="hand2")
# signup_link.pack()
# signup_link.bind("<Button-1>", lambda event: show_signup_frame())

import tkinter as tk
from tkinter import ttk
import main


def show_login_frame():
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    main.signup_frame.place_forget()


def login():
    # Retrieve entered username and password
    username = login_email_entry.get()
    password = password_entry.get()

    # Placeholder validation logic
    if username == "admin" and password == "password":
        # Successful login
        print("Login successful!")
        main.show_main_frame()
    else:
        # Invalid login
        print("Invalid username or password")


# Create the login frame
login_frame = ttk.Frame(main.window, padding=20)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add login widgets
login_email_label = ttk.Label(login_frame, text="Email:")
login_email_label.pack()
login_email_entry = ttk.Entry(login_frame)
login_email_entry.pack()

password_label = ttk.Label(login_frame, text="Password:")
password_label.pack()
password_entry = ttk.Entry(login_frame, show="*")
password_entry.pack()

login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.pack()

signup_link = ttk.Label(login_frame, text="Don't have an account? Sign up!", cursor="hand2")
signup_link.pack()
signup_link.bind("<Button-1>", lambda event: show_login_frame())

# Start the main loop
main.window.mainloop()

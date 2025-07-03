import customtkinter as ctk
from tkinter import messagebox


app = ctk.CTk()
app.title("waste log")
app.geometry("1000x600")

# stores users
users = {}

# sign up fuction
def signup():
    name = nameEntry.get()
    email = emailEntry.get()

    if not name or not email:
        messagebox.showerror("Error")
        return

    if email in users:
        messagebox.showinfo("Already Registered", "You are already signed up. Please login.")

# login fuction
def login():
    name = nameEntry.get()
    email = emailEntry.get()

    if not name or not email:
        messagebox.showerror("Error")
        return

    if email in users == name:
        messagebox.showinfo("Welcome")

# title
titleLabel = ctk.CTkLabel(app, text="waste track", font=("Henlvetica", 30))
titleLabel.pack(pady=20)

# name entry
nameEntry = ctk.CTkEntry(app, placeholder_text="name")
nameEntry.pack(pady=10, padx=20)

# email entry
emailEntry = ctk.CTkEntry(app, placeholder_text="email")
emailEntry.pack(pady=10, padx=20)

# login button
loginButton = ctk.CTkButton(app, text="login")
loginButton.pack(pady=10, padx=20)

# signup button
signupButton = ctk.CTkButton(app, text="sign up")
signupButton.pack(pady=10, padx=20)


app.mainloop()
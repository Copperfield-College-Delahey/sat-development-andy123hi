import customtkinter as ctk
from tkinter import messagebox


app = ctk.CTk()
app.title("waste log")
app.geometry("1000x600")

users = {}

def signup():
    name = nameEntry
    email = emailEntry

    if not name or not email:
        messagebox.showerror("Error")
        return

    if email in users:


def login():
    name = nameEntry
    email = emailEntry

titleLabel = ctk.CTkLabel(app, text="waste track", font=("Henlvetica", 30))
titleLabel.pack(pady=20)

nameEntry = ctk.CTkEntry(app, placeholder_text="name")
nameEntry.pack(pady=10, padx=20)

emailEntry = ctk.CTkEntry(app, placeholder_text="email")
emailEntry.pack(pady=10, padx=20)

loginButton = ctk.CTkButton(app, text="login")
loginButton.pack(pady=10, padx=20)

signupButton = ctk.CTkButton(app, text="sign up")
signupButton.pack(pady=10, padx=20)


app.mainloop()
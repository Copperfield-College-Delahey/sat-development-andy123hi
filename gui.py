import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.title("waste log")
app.geometry("1000x600")

titleLabel = ctk.CTkLabel(app, text="waste track", font=("Henlvetica", 30))
titleLabel.pack(pady=20)

nameEntry = ctk.CTkEntry(app, placeholder_text="name")
nameEntry.pack(pady=10, padx=20)

emailEntry = ctk.CTkEntry(app, placeholder_text="email")
emailEntry.pack(pady=10, padx=20)

app.mainloop()
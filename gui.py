import customtkinter as ctk
from tkinter import messagebox, ttk

app = ctk.CTk()
app.title("waste log")
app.geometry("1000x600")

topFrame = ctk.CTkFrame(app, border_width=4)
titleLabel = ctk.CTkLabel(topFrame, text="waste item", font=("Henlvetica", 30))

app.mainloop()
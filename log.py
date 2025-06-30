import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.title("waste log")
app.geometry("1000x600")

title = ctk.CTkLabel(app, text="waste track", font=("Arial", 20))
title.pack(pady=10)

wasteItemLabel = ctk.CTkLabel(app, text="waste item")
wasteItemLabel.pack(pady=10)

wasteItemEntry = ctk.CTkEntry(app)
wasteItemEntry.pack(pady=10)

categoryLabel = ctk.CTkLabel(app, text="category")
categoryLabel.pack(pady=10)

categoryMenu = ctk.CTkComboBox(app, values=["recyclable", "reuseable", "disposable"])
categoryMenu.pack(pady=10)

dateLabel = ctk.CTkLabel(app, text="date")
dateLabel.pack(pady=10)

app.mainloop()
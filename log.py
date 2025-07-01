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

dateEntry = ctk.CTkEntry(app)
dateEntry.pack(pady=10)

idontknowButton = ctk.CTkButton(app, text="I don't know")
idontknowButton.pack(pady=10)

askforhelpButton = ctk.CTkButton(app, text="Ask for Help")
askforhelpButton.pack(pady=10)

feedbackButton = ctk.CTkButton(app, text="Feedback")
feedbackButton.pack(pady=10)

saveButton = ctk.CTkButton(app, text="Save")
saveButton.pack(pady=10)

viewpastEntry = ctk.CTkButton(app, text="View past Entry")
viewpastEntry.pack(pady=10)

app.mainloop()
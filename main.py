import customtkinter as ctk
from tkinter import messagebox

wasteLog = []

# Fuctions
def suggestCategory():

def idk():
    item = itemEntry.get()
    if not item:
        messagebox.showwarning("Input needed", "Please enter a waste item first.")
        return
    suggestion = suggestCategory()
    if suggestion == "Unknown":
        messagebox.showinfo("Suggestion", "Could not determine category.")

def help():

def saveEntry():
    item = itemEntry.get()
    category =

def feedback():

def viweLogs():



# window
app = ctk.CTk()
app.title("waste log")
app.geometry("1000x600")

# title
title = ctk.CTkLabel(app, text="waste track", font=("Arial", 20))
title.pack(pady=10)

# waste item
wasteItemLabel = ctk.CTkLabel(app, text="waste item")
wasteItemLabel.pack(pady=10)

wasteItemEntry = ctk.CTkEntry(app)
wasteItemEntry.pack(pady=10)

# category
categoryLabel = ctk.CTkLabel(app, text="category")
categoryLabel.pack(pady=10)

# dropdown menu for categorys
categoryMenu = ctk.CTkComboBox(app, values=["recyclable", "reuseable", "disposable"])
categoryMenu.pack(pady=10)

# date
dateLabel = ctk.CTkLabel(app, text="date")
dateLabel.pack(pady=10)

dateEntry = ctk.CTkEntry(app)
dateEntry.pack(pady=10)

#  i dont know button
idontknowButton = ctk.CTkButton(app, text="I don't know")
idontknowButton.pack(pady=10)

# ask for help button
askforhelpButton = ctk.CTkButton(app, text="Ask for Help")
askforhelpButton.pack(pady=10)

# feedback button
feedbackButton = ctk.CTkButton(app, text="Feedback")
feedbackButton.pack(pady=10)

# save button
saveButton = ctk.CTkButton(app, text="Save")
saveButton.pack(pady=10)

# view past entry button
viewpastEntry = ctk.CTkButton(app, text="View past Entry")
viewpastEntry.pack(pady=10)

app.mainloop()
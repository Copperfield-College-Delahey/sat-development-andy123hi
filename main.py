import customtkinter as ctk
from tkinter import messagebox

# Waste log list
WasteLog = []

# Function to suggest category (stub)
def SuggestCategory():
    messagebox.showinfo("Suggestion", "Try checking the material. For example, plastic is usually recyclable.")

# "I Don't Know" button action
def Idk():
    Item = WasteItemEntry.get()
    if not Item:
        messagebox.showerror("Error", "Please enter the waste item first.")
    else:
        messagebox.showinfo("Hint", f"We're not sure what '{Item}' is. Try using the 'Ask for Help' button.")

# Help function
def Help():
    messagebox.showinfo("Help", "If you're unsure about your waste item, choose 'I don't know' or ask for help.\n\nExamples:\n- Plastic bottle = Recyclable\n- Food wrapper = Disposable")

# Save the log entry
def SaveEntry():
    end

# Feedback function
def Feedback():
    if not WasteLog:
        messagebox.showinfo("Feedback", "No entries yet.")
        return
    counts = {"Recyclable": 0, "Reuseable": 0, "Disposable": 0}
    for entry in WasteLog:
        category = entry["Category"].capitalize()
        if category in counts:
            counts[category] += 1
# View logs
def ViewLogs():
    end

# Window setup
App = ctk.CTk()
App.title("Waste Log")
App.geometry("1000x600")

# Title
Title = ctk.CTkLabel(App, text="Waste Track", font=("Arial", 24, "bold"))
Title.pack(pady=10)

# Waste item
WasteItemLabel = ctk.CTkLabel(App, text="Waste Item")
WasteItemLabel.pack(pady=5)
WasteItemEntry = ctk.CTkEntry(App, placeholder_text="Enter waste item")
WasteItemEntry.pack(pady=5)

# Category
CategoryLabel = ctk.CTkLabel(App, text="Category")
CategoryLabel.pack(pady=5)
CategoryMenu = ctk.CTkComboBox(App, values=["Recyclable", "Reuseable", "Disposable"])
CategoryMenu.pack(pady=5)

# Date


# Buttons
IdkButton = ctk.CTkButton(App, text="I Don't Know", command=Idk)
IdkButton.pack(pady=5)

AskForHelpButton = ctk.CTkButton(App, text="Ask for Help", command=Help)
AskForHelpButton.pack(pady=5)

FeedbackButton = ctk.CTkButton(App, text="Feedback", command=Feedback)
FeedbackButton.pack(pady=5)

SaveButton = ctk.CTkButton(App, text="Save", command=SaveEntry)
SaveButton.pack(pady=5)

ViewPastEntry = ctk.CTkButton(App, text="View Past Entry", command=ViewLogs)
ViewPastEntry.pack(pady=5)

# Start the app
App.mainloop()

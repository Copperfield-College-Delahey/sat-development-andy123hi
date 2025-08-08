import customtkinter as ctk
from tkinter import messagebox
import json
import os
from datetime import datetime

# App setup
app = ctk.CTk()
app.title("Waste Log")
app.geometry("1000x600")

# Stores users
userAccounts = {}
wasteLog = []

# Loads the previous users
if os.path.exists("users.json"):
    with open("users.json", "r") as f:
        userAccounts = json.load(f)

if os.path.exists("waste_log.json"):
    with open("waste_log.json", "r") as f:
        wasteLog = json.load(f)

# Switches between screens
def showFrame(frame):
    for widget in app.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

# Sign-up with email validation
def signUp():
    userName = nameEntry.get()
    userEmail = emailEntry.get()

    if not userName or not userEmail:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not userEmail.endswith("@gmail.com"):
        messagebox.showerror("Invalid Email", "Email must end with '@gmail.com'")
        return

    if userEmail in userAccounts:
        messagebox.showinfo("Already Registered", "You are already signed up.")
    else:
        userAccounts[userEmail] = userName
        with open("users.json", "w") as f:
            json.dump(userAccounts, f)
        messagebox.showinfo("Success", f"Signed up as {userName}")

# Login and go to waste log
def logIn():
    userName = nameEntry.get()
    userEmail = emailEntry.get()

    if not userName or not userEmail:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if userEmail in userAccounts and userAccounts[userEmail] == userName:
        messagebox.showinfo("Welcome", f"Hello, {userName}!")
        showFrame(wasteLogFrame)
    else:
        messagebox.showwarning("Failed", "Invalid login. Please sign up first.")

# Suggestion message
def suggestCategory():
    messagebox.showinfo("Suggestion", "Plastic is usually recyclable. Try checking the material.")

# 'I don't know' with keyword-based suggestions
def idk():
    item = wasteItemEntry.get().strip().lower()

    if not item:
        messagebox.showerror("Error", "Enter the waste item first.")
        return

    recyclableKeywords = ["plastic", "paper", "glass", "tin", "cardboard", "can", "jar", "bottle", "container"]
    disposableKeywords = ["wrapper", "foil", "peel", "tissue", "straw", "styrofoam", "napkin"]
    reusableKeywords = ["bag", "cloth", "tote", "reusable", "container", "box"]

    if any(word in item for word in recyclableKeywords):
        suggested = "Recyclable"
    elif any(word in item for word in disposableKeywords):
        suggested = "Disposable"
    elif any(word in item for word in reusableKeywords):
        suggested = "Reuseable"
    else:
        messagebox.showinfo("Suggestion", f"Not sure about '{item}'. Try using the Help button for general tips.")
        return

    messagebox.showinfo("Suggestion", f"The item '{item}' is likely categorized as '{suggested}'.")
    categoryMenu.set(suggested)

# Help popup
def helpInfo():
    messagebox.showinfo("Help", "Examples:\n- Plastic bottle = Recyclable\n- Food wrapper = Disposable")

# Date validation function
def validateDate(date_str):
    try:
        datetime.strptime(date_str, "%d %m %Y")
        return True
    except ValueError:
        return False

# Save waste entry with date validation
def saveEntry():
    item = wasteItemEntry.get()
    category = categoryMenu.get()
    date = dateEntry.get()

    if not item or not category or not date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not validateDate(date):
        messagebox.showerror("Invalid Date", "Date must be in the format 'DD MM YYYY' and valid.")
        return

    wasteLog.append({"Item": item, "Category": category, "Date": date})
    with open("waste_log.json", "w") as f:
        json.dump(wasteLog, f)
    messagebox.showinfo("Saved", f"Saved entry: {item} ({category}) on {date}")
    wasteItemEntry.delete(0, 'end')
    dateEntry.delete(0, 'end')

# Feedback
def feedback():
    if not wasteLog:
        messagebox.showinfo("Feedback", "No entries yet.")
        return

    counts = {"Recyclable": 0, "Reuseable": 0, "Disposable": 0}
    for entry in wasteLog:
        category = entry["Category"].capitalize()
        if category in counts:
            counts[category] += 1

    summary = "\n".join([f"{k}: {v}" for k, v in counts.items()])
    messagebox.showinfo("Feedback", f"Summary:\n\n{summary}")

# View past waste entries
def viewLogs():
    pastEntriesTextBox.delete("1.0", "end")
    if not wasteLog:
        pastEntriesTextBox.insert("end", "No past entries yet.")
    else:
        for i, entry in enumerate(wasteLog, start=1):
            pastEntriesTextBox.insert("end", f"{i}. {entry['Item']} ({entry['Category']}) on {entry['Date']}\n")
    showFrame(pastEntriesFrame)

# Login screen
loginFrame = ctk.CTkFrame(app)

ctk.CTkLabel(loginFrame, text="Waste Track", font=("Helvetica", 30)).pack(pady=20)

nameEntry = ctk.CTkEntry(loginFrame, placeholder_text="Name")
nameEntry.pack(pady=10, padx=20)

emailEntry = ctk.CTkEntry(loginFrame, placeholder_text="Email")
emailEntry.pack(pady=10, padx=20)

ctk.CTkButton(loginFrame, text="Login", command=logIn).pack(pady=10)
ctk.CTkButton(loginFrame, text="Sign Up", command=signUp).pack(pady=10)

# Waste logging screen
wasteLogFrame = ctk.CTkFrame(app)

ctk.CTkLabel(wasteLogFrame, text="Waste Log", font=("Arial", 24, "bold")).pack(pady=10)

wasteItemEntry = ctk.CTkEntry(wasteLogFrame, placeholder_text="Enter waste item")
wasteItemEntry.pack(pady=5)

categoryMenu = ctk.CTkComboBox(wasteLogFrame, values=["Recyclable", "Reuseable", "Disposable"])
categoryMenu.pack(pady=5)

dateEntry = ctk.CTkEntry(wasteLogFrame, placeholder_text="DD MM YYYY")
dateEntry.pack(pady=5)

ctk.CTkButton(wasteLogFrame, text="I Don't Know", command=idk).pack(pady=5)
ctk.CTkButton(wasteLogFrame, text="Ask for Help", command=helpInfo).pack(pady=5)
ctk.CTkButton(wasteLogFrame, text="Feedback", command=feedback).pack(pady=5)
ctk.CTkButton(wasteLogFrame, text="Save Entry", command=saveEntry).pack(pady=5)
ctk.CTkButton(wasteLogFrame, text="View Past Entry", command=viewLogs).pack(pady=5)
ctk.CTkButton(wasteLogFrame, text="Logout", command=lambda: showFrame(loginFrame)).pack(pady=5)

# Past entries screen
pastEntriesFrame = ctk.CTkFrame(app)

ctk.CTkLabel(pastEntriesFrame, text="Past Waste Entries", font=("Arial", 20, "bold")).pack(pady=10)
pastEntriesTextBox = ctk.CTkTextbox(pastEntriesFrame, width=600, height=300)
pastEntriesTextBox.pack(pady=10)

ctk.CTkButton(pastEntriesFrame, text="Back to Waste Log", command=lambda: showFrame(wasteLogFrame)).pack(pady=10)

# Start at login
showFrame(loginFrame)

app.mainloop()

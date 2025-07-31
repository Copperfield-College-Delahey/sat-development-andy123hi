import customtkinter as ctk
from tkinter import messagebox

# Initialize the window
App = ctk.CTk()
App.title("Waste Log")
App.geometry("1000x600")

# Store user data
UserAccounts = {}

# Switch Screens
def ShowFrame(frame):
    for widget in App.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

# Sign-up function
def SignUp():
    UserName = NameEntry.get()
    UserEmail = EmailEntry.get()

    if not UserName or not UserEmail:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if UserEmail in UserAccounts:
        messagebox.showinfo("Already Registered", "You are already signed up. Please login.")
    else:
        UserAccounts[UserEmail] = UserName
        messagebox.showinfo("Success", f"Signed up as {UserName}")

# Login function
def LogIn():
    UserName = NameEntry.get()
    UserEmail = EmailEntry.get()

    if not UserName or not UserEmail:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if UserEmail in UserAccounts and UserAccounts[UserEmail] == UserName:
        messagebox.showinfo("Welcome", f"Hello, {UserName}! You're now logged in.")

    else:
        messagebox.showwarning("Failed", "Invalid login. Please sign up first.")

# Login Screen
LoginFrame = ctk.CTkFrame(App)

# Title label
TitleLabel = ctk.CTkLabel(LoginFrame, text="Waste Track", font=("Helvetica", 30))
TitleLabel.pack(pady=20)

# Name entry
NameEntry = ctk.CTkEntry(LoginFrame, placeholder_text="Name")
NameEntry.pack(pady=10, padx=20)

# Email entry
EmailEntry = ctk.CTkEntry(LoginFrame, placeholder_text="Email")
EmailEntry.pack(pady=10, padx=20)

# Login button
LoginButton = ctk.CTkButton(LoginFrame, text="Login", command=LogIn)
LoginButton.pack(pady=10, padx=20)

# Signup button
SignUpButton = ctk.CTkButton(LoginFrame, text="Sign Up", command=SignUp)
SignUpButton.pack(pady=10, padx=20)

# Waste Log Screen
wasteLogFrame = ctk.CTkFrame(App)

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


# Title
Title = ctk.CTkLabel(wasteLogFrame, text="Waste Track", font=("Arial", 24, "bold"))
Title.pack(pady=10)

# Waste item
WasteItemLabel = ctk.CTkLabel(wasteLogFrame, text="Waste Item")
WasteItemLabel.pack(pady=5)
WasteItemEntry = ctk.CTkEntry(wasteLogFrame, placeholder_text="Enter waste item")
WasteItemEntry.pack(pady=5)

# Category
CategoryLabel = ctk.CTkLabel(wasteLogFrame, text="Category")
CategoryLabel.pack(pady=5)
CategoryMenu = ctk.CTkComboBox(wasteLogFrame, values=["Recyclable", "Reuseable", "Disposable"])
CategoryMenu.pack(pady=5)

# Date


# Buttons
IdkButton = ctk.CTkButton(wasteLogFrame, text="I Don't Know", command=Idk)
IdkButton.pack(pady=5)

AskForHelpButton = ctk.CTkButton(wasteLogFrame, text="Ask for Help", command=Help)
AskForHelpButton.pack(pady=5)

FeedbackButton = ctk.CTkButton(wasteLogFrame, text="Feedback", command=Feedback)
FeedbackButton.pack(pady=5)

SaveButton = ctk.CTkButton(wasteLogFrame, text="Save", command=SaveEntry)
SaveButton.pack(pady=5)

ViewPastEntry = ctk.CTkButton(wasteLogFrame, text="View Past Entry", command=ViewLogs)
ViewPastEntry.pack(pady=5)


ShowFrame(LoginFrame)

# Run the app
App.mainloop()

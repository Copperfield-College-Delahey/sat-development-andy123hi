import customtkinter as ctk
from tkinter import messagebox

# Initialize the window
App = ctk.CTk()
App.title("Waste Log")
App.geometry("1000x600")

# Store user data
UserAccounts = {}

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

# Title label
TitleLabel = ctk.CTkLabel(App, text="Waste Track", font=("Helvetica", 30))
TitleLabel.pack(pady=20)

# Name entry
NameEntry = ctk.CTkEntry(App, placeholder_text="Name")
NameEntry.pack(pady=10, padx=20)

# Email entry
EmailEntry = ctk.CTkEntry(App, placeholder_text="Email")
EmailEntry.pack(pady=10, padx=20)

# Login button
LoginButton = ctk.CTkButton(App, text="Login", command=LogIn)
LoginButton.pack(pady=10, padx=20)

# Signup button
SignUpButton = ctk.CTkButton(App, text="Sign Up", command=SignUp)
SignUpButton.pack(pady=10, padx=20)

# Run the app
App.mainloop()

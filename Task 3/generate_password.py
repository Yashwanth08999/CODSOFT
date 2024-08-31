import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Define the character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_characters = letters + digits + symbols
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def on_generate_click():
    try:
        # Get the length from the entry widget
        length = int(length_entry.get())
        
        # Generate the password
        password = generate_password(length)
        
        # Display the password in the result label
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Configure the main window
root.geometry("400x300")  # Set window size (width x height)
root.configure(bg="#f0f0f0")  # Set background color

# Create and place the widgets
length_label = tk.Label(root, text="Enter the desired length of the password:", bg="#f0f0f0", font=("Helvetica", 12))
length_label.pack(pady=15)

length_entry = tk.Entry(root, font=("Helvetica", 12), width=20)
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=on_generate_click, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", padx=10, pady=5)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="Generated Password will appear here", bg="#f0f0f0", font=("Helvetica", 12))
result_label.pack(pady=15)

# Start the Tkinter event loop
root.mainloop()

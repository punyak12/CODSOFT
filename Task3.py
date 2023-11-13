import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_password_button_click():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        generated_password = generate_password(password_length)
        result_label.config(text="Generated Password: " + generated_password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(window, text="Enter the desired length of the password:")
length_label.pack(pady=10)

length_entry = tk.Entry(window)
length_entry.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_click)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main loop
window.mainloop()





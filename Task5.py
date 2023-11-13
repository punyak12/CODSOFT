import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("410x490")

        self.contacts = []

        # Labels and Entry Widgets
        self.name_label = tk.Label(root, text="NAME :")
        self.name_entry = tk.Entry(root, width=40)

        self.phone_label = tk.Label(root, text="PHONE NO. :")
        self.phone_entry = tk.Entry(root, width=40)

        self.email_label = tk.Label(root, text="EMAIL:")
        self.email_entry = tk.Entry(root, width=40)

        self.address_label = tk.Label(root, text="ADDRESS :")
        self.address_entry = tk.Entry(root, width=40)

        self.search_label = tk.Label(root, text="Search by Name:")
        self.search_entry = tk.Entry(root, width=30)

        # New entry for updating phone number
        self.new_phone_label = tk.Label(root, text="New Phone:")
        self.new_phone_entry = tk.Entry(root, width=40)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Grid Layout
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.search_entry.grid(row=6, column=1, padx=10, pady=10)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=8, column=0, columnspan=2, pady=10)
        self.new_phone_label.grid(row=9, column=0, padx=10, pady=10, sticky="e")
        self.new_phone_entry.grid(row=9, column=1, padx=10, pady=10)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone are required.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact['name']} - {contact['phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = self.search_entry.get()
        search_results = [contact for contact in self.contacts if
                          search_term.lower() in contact['name'].lower()]

        if not search_results:
            messagebox.showinfo("Info", "No matching contacts found.")
        else:
            search_list = "\n".join([f"{contact['name']} - {contact['phone']}" for contact in search_results])
            messagebox.showinfo("Search Results", search_list)

    def update_contact(self):
        name = self.name_entry.get()
        new_phone = self.new_phone_entry.get()

        for contact in self.contacts:
            if contact['name'] == name:
                contact['phone'] = new_phone
                messagebox.showinfo("Success", "Contact updated successfully.")
                return

        messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()

        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        messagebox.showinfo("Success", "Contact deleted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

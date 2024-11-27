import tkinter as tk
from tkinter import messagebox, ttk

# Global Data Store (In-memory for simplicity)
users = {"admin": "admin123"}  # Predefined user
inventory = {}

# Functions
def authenticate_user(username, password):
    return users.get(username) == password

def add_product(product_id, name, quantity):
    if product_id in inventory:
        messagebox.showerror("Error", "Product ID already exists.")
    else:
        inventory[product_id] = {"name": name, "quantity": int(quantity)}
        messagebox.showinfo("Success", "Product added successfully!")

def edit_product(product_id, name, quantity):
    if product_id in inventory:
        inventory[product_id] = {"name": name, "quantity": int(quantity)}
        messagebox.showinfo("Success", "Product updated successfully!")
    else:
        messagebox.showerror("Error", "Product ID does not exist.")

def delete_product(product_id):
    if product_id in inventory:
        del inventory[product_id]
        messagebox.showinfo("Success", "Product deleted successfully!")
    else:
        messagebox.showerror("Error", "Product ID does not exist.")

def generate_low_stock_report():
    report = [f"ID: {pid}, Name: {details['name']}, Quantity: {details['quantity']}" 
              for pid, details in inventory.items() if details['quantity'] < 10]
    return "\n".join(report) if report else "No low-stock items."

# GUI Functions
def login():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate_user(username, password):
        main_window()
    else:
        messagebox.showerror("Error", "Invalid credentials.")

def add_product_gui():
    product_id = product_id_entry.get()
    name = name_entry.get()
    quantity = quantity_entry.get()
    if not product_id or not name or not quantity.isdigit():
        messagebox.showerror("Error", "Invalid input. Please fill all fields correctly.")
        return
    add_product(product_id, name, quantity)
    refresh_inventory_table()

def edit_product_gui():
    product_id = product_id_entry.get()
    name = name_entry.get()
    quantity = quantity_entry.get()
    if not product_id or not name or not quantity.isdigit():
        messagebox.showerror("Error", "Invalid input. Please fill all fields correctly.")
        return
    edit_product(product_id, name, quantity)
    refresh_inventory_table()

def delete_product_gui():
    product_id = product_id_entry.get()
    if not product_id:
        messagebox.showerror("Error", "Please provide a Product ID.")
        return
    delete_product(product_id)
    refresh_inventory_table()

def refresh_inventory_table():
    for row in inventory_table.get_children():
        inventory_table.delete(row)
    for pid, details in inventory.items():
        inventory_table.insert("", "end", values=(pid, details['name'], details['quantity']))

def main_window():
    login_window.destroy()
    global product_id_entry, name_entry, quantity_entry, inventory_table

    # Main Window
    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("600x400")

    # Form Section
    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Product ID:").grid(row=0, column=0, padx=5, pady=5)
    product_id_entry = tk.Entry(form_frame)
    product_id_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
    quantity_entry = tk.Entry(form_frame)
    quantity_entry.grid(row=2, column=1, padx=5, pady=5)

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add Product", command=add_product_gui).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Edit Product", command=edit_product_gui).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Delete Product", command=delete_product_gui).grid(row=0, column=2, padx=10)
    tk.Button(button_frame, text="Low Stock Report", command=lambda: messagebox.showinfo("Low Stock Report", generate_low_stock_report())).grid(row=0, column=3, padx=10)

    # Inventory Table
    inventory_table = ttk.Treeview(root, columns=("ID", "Name", "Quantity"), show="headings")
    inventory_table.heading("ID", text="ID")
    inventory_table.heading("Name", text="Name")
    inventory_table.heading("Quantity", text="Quantity")
    inventory_table.pack(fill="both", expand=True, pady=10)

    refresh_inventory_table()
    root.mainloop()

# Login Window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

tk.Button(login_window, text="Login", command=login).pack(pady=20)

login_window.mainloop()

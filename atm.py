import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Interface")
        self.master.geometry("400x400")

        # PIN, Initial Balance, and Transaction History
        self.correct_pin = "1234"
        self.balance = 1000
        self.transaction_history = []

        # Show the welcome page
        self.show_welcome_page()

    def show_welcome_page(self):
        # Clear the window
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Welcome to the ATM", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.master, text="Please press 'Enter' to proceed", font=("Arial", 12)).pack(pady=10)

        enter_btn = tk.Button(self.master, text="Enter", font=("Arial", 12), command=self.show_pin_entry)
        enter_btn.pack(pady=20)

    def show_pin_entry(self):
        # Clear the window
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Enter your PIN", font=("Arial", 18)).pack(pady=20)
        self.pin_entry = tk.Entry(self.master, show="*", font=("Arial", 12), width=20)
        self.pin_entry.pack(pady=10)

        submit_btn = tk.Button(self.master, text="Submit", font=("Arial", 12), command=self.validate_pin)
        submit_btn.pack(pady=20)

    def validate_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.correct_pin:
            self.show_main_interface()
        else:
            messagebox.showerror("Error", "Invalid PIN! Please try again.")

    def show_main_interface(self):
        # Clear the window
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Welcome to the ATM", font=("Arial", 18)).pack(pady=20)

        self.balance_btn = tk.Button(self.master, text="Check Balance", command=self.check_balance, width=20, font=("Arial", 12))
        self.balance_btn.pack(pady=10)

        self.deposit_btn = tk.Button(self.master, text="Deposit", command=self.deposit, width=20, font=("Arial", 12))
        self.deposit_btn.pack(pady=10)

        self.withdraw_btn = tk.Button(self.master, text="Withdraw", command=self.withdraw, width=20, font=("Arial", 12))
        self.withdraw_btn.pack(pady=10)

        self.history_btn = tk.Button(self.master, text="Transaction History", command=self.view_history, width=20, font=("Arial", 12))
        self.history_btn.pack(pady=10)

        self.exit_btn = tk.Button(self.master, text="Exit", command=self.confirm_exit, width=20, font=("Arial", 12))
        self.exit_btn.pack(pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance Inquiry", f"Your current balance is: ₹{self.balance}")

    def deposit(self):
        deposit_window = tk.Toplevel(self.master)
        deposit_window.title("Deposit")
        deposit_window.geometry("300x200")

        tk.Label(deposit_window, text="Enter amount to deposit:", font=("Arial", 12)).pack(pady=10)
        amount_entry = tk.Entry(deposit_window, font=("Arial", 12))
        amount_entry.pack(pady=10)

        def perform_deposit():
            try:
                amount = float(amount_entry.get())
                if amount > 0:
                    self.balance += amount
                    self.transaction_history.append(f"Deposited: ₹{amount}")
                    messagebox.showinfo("Success", f"₹{amount} deposited successfully!")
                    deposit_window.destroy()
                else:
                    messagebox.showerror("Error", "Enter a valid amount!")
            except ValueError:
                messagebox.showerror("Error", "Enter a numeric value!")

        deposit_btn = tk.Button(deposit_window, text="Deposit", command=perform_deposit, font=("Arial", 12))
        deposit_btn.pack(pady=10)

    def withdraw(self):
        withdraw_window = tk.Toplevel(self.master)
        withdraw_window.title("Withdraw")
        withdraw_window.geometry("300x200")

        tk.Label(withdraw_window, text="Enter amount to withdraw:", font=("Arial", 12)).pack(pady=10)
        amount_entry = tk.Entry(withdraw_window, font=("Arial", 12))
        amount_entry.pack(pady=10)

        def perform_withdrawal():
            try:
                amount = float(amount_entry.get())
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    self.transaction_history.append(f"Withdrawn: ₹{amount}")
                    messagebox.showinfo("Success", f"₹{amount} withdrawn successfully!")
                    withdraw_window.destroy()
                elif amount > self.balance:
                    messagebox.showerror("Error", "Insufficient balance!")
                else:
                    messagebox.showerror("Error", "Enter a valid amount!")
            except ValueError:
                messagebox.showerror("Error", "Enter a numeric value!")

        withdraw_btn = tk.Button(withdraw_window, text="Withdraw", command=perform_withdrawal, font=("Arial", 12))
        withdraw_btn.pack(pady=10)

    def view_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Transaction History")
        history_window.geometry("400x300")

        tk.Label(history_window, text="Transaction History", font=("Arial", 16)).pack(pady=10)

        if not self.transaction_history:
            tk.Label(history_window, text="No transactions yet.", font=("Arial", 12)).pack(pady=10)
        else:
            history_text = tk.Text(history_window, font=("Arial", 12), height=15, width=40)
            history_text.pack(pady=10)
            history_text.insert(tk.END, "\n".join(self.transaction_history))
            history_text.config(state=tk.DISABLED)

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.quit()

# Create the main window
root = tk.Tk()
atm = ATM(root)
root.mainloop()

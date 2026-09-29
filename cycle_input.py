import tkinter as tk
from tkinter import messagebox

from validation import validate_date, validate_number
from storage import save_cycle


def add_cycle(window, update_dashboard):

    cycle_window = tk.Toplevel(window)
    cycle_window.title("Add New Cycle")
    cycle_window.geometry("500x500")
    cycle_window.configure(bg="#D8C8F0")

    cycle_title = tk.Label(
        cycle_window,
        text="Add New Cycle",
        font=("Segoe UI", 20, "bold"),
        bg="#D8C8F0",
        fg="black")

    cycle_title.pack(
        anchor="w",
        padx=30,
        pady=(30, 20))


    date_label = tk.Label(
        cycle_window,
        text="Last Period Date",
        font=("Segoe UI", 11, "bold"),
        bg="#D8C8F0",
        fg="black")

    date_label.pack(
        anchor="w",
        padx=30,
        pady=(10, 5))


    date_entry = tk.Entry(
        cycle_window,
        font=("Segoe UI", 11),
        width=30)

    date_entry.pack(
        anchor="w",
        padx=30)


    cycle_length_label = tk.Label(
        cycle_window,
        text="Cycle Length (days)",
        font=("Segoe UI", 11, "bold"),
        bg="#D8C8F0",
        fg="black")

    cycle_length_label.pack(
        anchor="w",
        padx=30,
        pady=(20, 5))


    cycle_length_entry = tk.Entry(
        cycle_window,
        font=("Segoe UI", 11),
        width=30)

    cycle_length_entry.pack(
        anchor="w",
        padx=30)


    period_duration_label = tk.Label(
        cycle_window,
        text="Period Duration (days)",
        font=("Segoe UI", 11, "bold"),
        bg="#D8C8F0",
        fg="black")

    period_duration_label.pack(
        anchor="w",
        padx=30,
        pady=(20, 5))


    period_duration_entry = tk.Entry(
        cycle_window,
        font=("Segoe UI", 11),
        width=30)

    period_duration_entry.pack(
        anchor="w",
        padx=30)


    def save_data():

        date = date_entry.get()
        cycle_length = cycle_length_entry.get()
        period_duration = period_duration_entry.get()

        if not validate_date(date):
            messagebox.showerror(
                "Error",
                "Enter date in DD/MM/YYYY format.")
            return

        if not validate_number(cycle_length):
            messagebox.showerror(
                "Error",
                "Enter a valid cycle length.")
            return

        if not validate_number(period_duration):
            messagebox.showerror(
                "Error",
                "Enter a valid period duration.")
            return

        cycle_data = {
            "last_period": date,
            "cycle_length": int(cycle_length),
            "period_duration": int(period_duration)
        }

        save_cycle(cycle_data)

        update_dashboard(cycle_data)

        messagebox.showinfo(
            "Saved",
            "Cycle information saved successfully.")

        cycle_window.destroy()


    save_button = tk.Button(
        cycle_window,
        text="Save Cycle",
        font=("Segoe UI", 11, "bold"),
        bg="#D81B60",
        fg="white",
        padx=20,
        pady=10,
        command=save_data)

    save_button.pack(
        anchor="w",
        padx=30,
        pady=30)
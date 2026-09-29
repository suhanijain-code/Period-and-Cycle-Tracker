import tkinter as tk

from storage import get_cycles


def view_history(window):

    history_window = tk.Toplevel(window)
    history_window.title("Cycle History")
    history_window.geometry("600x500")
    history_window.configure(bg="#D8C8F0")


    history_title = tk.Label(
        history_window,
        text="Cycle History",
        font=("Segoe UI", 20, "bold"),
        bg="#D8C8F0",
        fg="black")

    history_title.pack(
        anchor="w",
        padx=30,
        pady=(30, 20))


    cycles = get_cycles()


    if len(cycles) == 0:

        message = tk.Label(
            history_window,
            text="No cycle records found.",
            font=("Segoe UI", 12),
            bg="#D8C8F0",
            fg="black")

        message.pack(
            padx=30,
            pady=20)


    else:

        for number, cycle in enumerate(
                cycles,
                start=1):

            record = tk.Label(
                history_window,
                text=(
                    f"Record {number}\n"
                    f"Last Period: {cycle['last_period']}\n"
                    f"Cycle Length: "
                    f"{cycle['cycle_length']} days\n"
                    f"Period Duration: "
                    f"{cycle['period_duration']} days"
                ),
                font=("Segoe UI", 11),
                bg="white",
                justify="left",
                padx=20,
                pady=15)

            record.pack(
                fill="x",
                padx=30,
                pady=8)
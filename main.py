import tkinter as tk

from cycle_input import add_cycle
from history import view_history
from storage import get_cycles
from calculations import calculate_next_period, calculate_cycle_day


window = tk.Tk()

window.title("Period & Cycle Tracker")
window.geometry("900x600")
window.configure(bg="#D8C8F0")


def update_dashboard(cycle_data):

    next_period = calculate_next_period(
        cycle_data["last_period"],
        cycle_data["cycle_length"])

    cycle_day = calculate_cycle_day(
        cycle_data["last_period"])

    next_period_value.config(
        text=next_period)

    cycle_length_value.config(
        text=f"{cycle_data['cycle_length']} days")

    cycle_day_value.config(
        text=str(cycle_day))


title_label = tk.Label(
    window,
    text="❤️Period & Cycle Tracker ✨",
    font=("Segoe UI", 24, "bold"),
    bg="#D8C8F0",
    fg="black")

title_label.pack(
    anchor="w",
    padx=30,
    pady=(30, 5))


subtitle_label = tk.Label(
    window,
    text="Track your cycle and keep your records organized.",
    font=("Segoe UI", 11),
    bg="#D8C8F0",
    fg="black")

subtitle_label.pack(
    anchor="w",
    padx=30)


cards_frame = tk.Frame(
    window,
    bg="#D8C8F0")

cards_frame.pack(
    anchor="w",
    padx=30,
    pady=40)


next_period_card = tk.Frame(
    cards_frame,
    bg="white",
    bd=1,
    relief="raised",
    highlightbackground="#DB3D77",
    highlightthickness=2,
    padx=45,
    pady=35)

next_period_card.pack(
    side="left",
    padx=(0, 20))


next_period_title = tk.Label(
    next_period_card,
    text="NEXT PERIOD",
    font=("Segoe UI", 10, "bold"),
    bg="white")

next_period_title.pack(
    anchor="w")


next_period_value = tk.Label(
    next_period_card,
    text="Not calculated",
    font=("Segoe UI", 18, "bold"),
    bg="white")

next_period_value.pack(
    anchor="w",
    pady=(8, 0))


cycle_length_card = tk.Frame(
    cards_frame,
    bg="white",
    highlightbackground="#D81B60",
    highlightthickness=2,
    padx=45,
    pady=35)

cycle_length_card.pack(
    side="left",
    padx=10)


cycle_length_title = tk.Label(
    cycle_length_card,
    text="CYCLE LENGTH",
    font=("Segoe UI", 10, "bold"),
    bg="white")

cycle_length_title.pack(
    anchor="w")


cycle_length_value = tk.Label(
    cycle_length_card,
    text="28 days",
    font=("Segoe UI", 18, "bold"),
    bg="white")

cycle_length_value.pack(
    anchor="w",
    pady=(8, 0))


cycle_day_card = tk.Frame(
    cards_frame,
    bg="white",
    highlightbackground="#D81B60",
    highlightthickness=2,
    padx=45,
    pady=35)

cycle_day_card.pack(
    side="left",
    padx=10)


cycle_day_title = tk.Label(
    cycle_day_card,
    text="CYCLE DAY",
    font=("Segoe UI", 10, "bold"),
    bg="white")

cycle_day_title.pack(
    anchor="w")


cycle_day_value = tk.Label(
    cycle_day_card,
    text="Not calculated",
    font=("Segoe UI", 18, "bold"),
    bg="white")

cycle_day_value.pack(
    anchor="w",
    pady=(8, 0))


buttons_frame = tk.Frame(
    window,
    bg="#D8C8F0")

buttons_frame.pack(
    anchor="w",
    padx=30,
    pady=20)


add_cycle_button = tk.Button(
    buttons_frame,
    text="Add New Cycle",
    font=("Segoe UI", 11, "bold"),
    bg="#D81B60",
    fg="white",
    padx=20,
    pady=10,
    command=lambda: add_cycle(window, update_dashboard))

add_cycle_button.pack(
    side="left",
    padx=(0, 15))


history_button = tk.Button(
    buttons_frame,
    text="View History",
    font=("Segoe UI", 11, "bold"),
    bg="#D81B60",
    fg="white",
    padx=20,
    pady=10,
    command=lambda: view_history(window))

history_button.pack(
    side="left")


cycles = get_cycles()

if len(cycles) > 0:
    update_dashboard(cycles[-1])


window.mainloop()
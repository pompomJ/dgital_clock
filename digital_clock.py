import datetime
import tkinter as tk
def update_time():
    now = datetime.datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    root.after(1000, update_time)
root = tk.Tk()
root.title("デジタル時計")
time_label = tk.Label(root, font=("Helvetica", 120), bg="white", fg="black")
time_label.pack(fill="both", expand=True)
update_time()
root.mainloop()

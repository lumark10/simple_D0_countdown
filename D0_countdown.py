#countdowm widget
import tkinter as tk
from datetime import datetime
import time

D0 = datetime(2027, 8, 31) #D-0 date

def get_days_left():
    now =datetime.now()
    delta = D0 - now
    return f"D-0: {delta.days} days left"

def update():
    label.config(text=get_days_left())
    root.after(60000, update) #update every minute

root = tk.Tk()
root.title("D-0 Countdown")
root.geometry("300x100")
root.attributes("-topmost", True) #keep on top of other windows
root.overrideredirect(True) #remove window borders
root.configure(bg='black')
root.attributes('-alpha', 0.8) #set transparency

#move window by dragging
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

label = tk.Label(root, text=get_days_left(), font=("Segoe UI", 24, "bold"), fg="#FFD369", bg="#222831")
label.pack(expand=True, fill="both")

#make label draggable
label.bind("<B1-Motion>", move_window)

#close widget with double-click
label.bind("<Double-Button-1>", lambda e: root.destroy())

update()
root.mainloop()
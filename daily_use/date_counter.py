import datetime
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root_title = "geri sayaç"


now = datetime.datetime.now()

# Correct the formatting string for day
day = now.strftime("%Y %m %d")  # %m for month and %d for day

# Parse the choosen_day string to a datetime object
choosen_day = datetime.datetime.strptime("2024.x.x", "%Y.%m.%d")
choosen_day2 = datetime.datetime.strptime("2024.x.x", "%Y.%m.%d")

# Calculate the difference without weekends
middle = choosen_day - now
weeks = int(middle.days / 7)
left= middle.days - weeks*2

#with weekends
middle2 = choosen_day2 -now


canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

canvas.create_rectangle(50,50,250,250, fill="black")
day_text = f"Kalan süre\n:       {left} gün"
canvas.create_text(150, 150, text=day_text, fill="white", font=("Helvetica", 8))


canvas2= tk.Canvas(root, width=300, height=300, bg="white")
canvas2.pack()
canvas2.create_rectangle(50,50,250,250, fill="white")
day_text2 = f"Kalan süre\n:        {middle2.days} gün"
canvas2.create_text(150, 150, text=day_text2, fill="black", font=("Helvetica", 8))


root.mainloop()
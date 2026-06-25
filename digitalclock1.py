import tkinter as tk
from time import strftime
import random

root=tk.Tk()
root.title("SMART DIGITAL CLOCK")
root.geometry==("900 x 400")
root.configure(bg="black")


colours=["cyan","red","lime","yellow","orange","pink","white","grey","violet"]

def greeting_message(hour):
    if hour<12:
        return "GOOD MORNING"
    elif hour<18:
        return "GOOD  AFTERNOON"
    else :
        return "GOOD NGHT"

def time():
    current_time=strftime("%H:%M:%S  %p")
    current_date=strftime("%A, %d %B %Y")
    hour=int(strftime("%H"))
    greeting=greeting_message(hour)

    random_colour=random.choice(colours)


    clock_label.config(
        text=current_time,
        fg=random_colour
    )

    date_label.config(
        text=current_date,
        fg="white"
    )

    
    greeting_label.config(
        text=greeting,
        fg="violet"
    )


    clock_label.after(1000,time)



title_label =tk.Label(root,
                      text="SMART DIGITAL CLOCK",
                      font=("ARIAL", 28, "bold"),
                      bg="black",
                      fg="orange"
                      )
title_label.pack(pady=10)


greeting_label =tk.Label(root,
                          font=("ARIAL", 28, "bold"),
                          bg="black",
                     )

greeting_label.pack(pady=10)


clock_label =tk.Label(root,
                    font=("Calibari", 70, "bold"),
                      bg="black",
                     )


clock_label.pack(pady=20)


date_label =tk.Label(root,
                      font=("ARIAL", 20),
                      bg="black",
                      )


date_label.pack(pady=10)

footer_label =tk.Label(root,
                      text="PYTHON TINKTER PROJECT",
                      font=("ARIAL", 14),
                      bg="black",
                      fg="gray"
                      )
footer_label.pack(side="bottom" , pady=10)

time()

root.mainloop()
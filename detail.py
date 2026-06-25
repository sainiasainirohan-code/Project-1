import tkinter 

def summit():
    print("summited")
root=tkinter.Tk()
root.title("Detail box")
root.geometry("400x300")
root.configure(bg="white")

name_box=tkinter.Label(root,text="Enter your name",fg="red")
name_box.pack()

name_box=tkinter.Entry(root)
name_box.pack()

email_box=tkinter.Label(root,text="Enter your email_ID",fg="blue")
email_box.pack()

email_box=tkinter.Entry(root)
email_box.pack()

mobile_number=tkinter.Label(root,text="Enter your mobile_number",fg="green")
mobile_number.pack()

mobile_number=tkinter.Entry(root)
mobile_number.pack()

course_name=tkinter.Label(root,text="Your course name",fg="violet")
course_name.pack()

course_name=tkinter.Entry(root)
course_name.pack()

button=tkinter.Button(root,text="summit",command=summit,fg="black",bg="grey")
button.pack()


root.mainloop()



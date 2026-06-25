from tkinter import*
import pyttsx3
import datetime

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_response():
    user_message=entry.get().lower()
    chat.insert(END,user_message)
    entry.delete(0,END)
    
    if "hello" in user_message:
        response="Hello Rohan sir ,how are you"
    
    elif "hi" in user_message:
        response="HI what can i do for you"
    elif"time" in user_message:
        CURRENT=datetime.datetime.now().strftime("%H:%M")
        response="current time is"+CURRENT
    elif "date" in user_message:
        CURRENT=datetime.datetime.now().strftime("%d-%m-%Y")
        response="today date is "+CURRENT
    elif"rohan" in user_message:
        response="Hello Rohan sir , I am your personal assistent Roy"
    elif "bye" in user_message:
        response="bye sir, always keep smile on yur  face"
    else:
        response=" Sorry i do not understand"
    chat.insert(END, "Roy: " + response + "\n\n")

    speak(response)

root=Tk()
root.title("Roy")
root.geometry("400x300")
root.config(bg="black")
root.bind("<Return>", lambda event: get_response())

chat = Text(root, width=20, height=10, font=("Arial", 12))
chat.pack()


entry = Entry(root, width=15, font=("Arial", 18))
entry.pack(pady=10)

send = Button(root, text="Send", command=get_response,fg="green", font=("Arial", 14))
send.pack()

root.mainloop()
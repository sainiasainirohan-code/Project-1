def get_response():
    user_message=entry.get().lower()
    chat.insert(END,user_message)
    entry.delete(0,END)
    
    if "hello" in user_message:
        response="Hello Rohan sir ,how are you"
    
    elif "hi" in user_message:
        response="HI what can i do for you"
    elif"time" in user_message:
        CURRENT=datetime.datetime.now().strftime("%H:%M:%S")
        response="current time is"+CURRENT
    elif "date" in user_message:
        CURRENT=datetime.datetime.now().strftime("%d-%m-%Y")
        response="today date is "+CURRENT
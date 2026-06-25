from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("notepad")
root.configure(background='Black')
root.geometry("500x400")
def new_password():
    user_creat_pw=input("Enter your password:")
    with open("pass.txt","w") as file:
        file.write(user_creat_pw)
def write_secret():
    pw=input("Entar your password")
    with open("pass.txt","r")as file:
        saved_pw=file.read()
    print("password match")
    if pw==saved_pw:
        msg=input("Enter your Secret note:")
        with open("uv.txt","w")as file:
            file.write(msg)
    else:
        print("password not matched")
def read_secret():
    pw=input("Enter your password:")
    with open("pass.txt","r")as file:
        saved_pw=file.read()
    if pw==saved_pw:
        with open("uv.txt","r")as file:
            print(file.read())
    else:
        print("wrong password")
while True:    
    print("""
      1.create password
      2.create secret message
      3.Read a secret message
      4.Exit
      """)        
    choice=input("enter your choice:")      
    if choice=="1":
        new_password()
    elif choice=="2":
        write_secret()
    elif choice=="3":
        read_secret()
    elif choice=="4":
        print("exiting...")
        break
    else :
        print("enter correct option")
label =Label(root,font=('calibri',70,'bold'),background='gray',foreground='black')
label.pack()
root.mainloop()     
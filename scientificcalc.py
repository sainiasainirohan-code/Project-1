from tkinter import *
import math
root=Tk()
root.title("my calculator")
root.geometry("300x200")
display=Entry(root,width=20,font=("Arial",20))
display.grid(row=0,column=0,columnspan=6)
def seven():
    display.insert(END,"7")
def eight():
    display.insert(END,"8")
def nine():
    display.insert(END,"9")
def six():
    display.insert(END,"6")
def five():
    display.insert(END,"5")
def four():
    display.insert(END,"4")
def three():
    display.insert(END,"3")
def two():
    display.insert(END,"2")
def one():
    display.insert(END,"1")
def plus():
    display.insert(END,"+")
def minus():
    display.insert(END,"-")
def mult():
    display.insert(END,"*")
def divide():
    display.insert(END,"/")
def zero():
    display.insert(END,"0")
def sin_function():
    display.delete(0, END)
    display.insert(0, "sin ")

def cos_function():
    display.delete(0, END)
    display.insert(0, "cos ")

def tan_function():
    display.delete(0, END)
    display.insert(0, "tan ")

def cot_function():
    display.delete(0, END)
    display.insert(0, "cot ")

def sec_function():
    display.delete(0, END)
    display.insert(0, "sec ")

def cosec_function():
    display.delete(0, END)
    display.insert(0, "cosec ")

def power_function():
    display.insert(END, "**")

def root_function():
    display.delete(0, END)
    display.insert(0, "sqrt ")
def equal():
    try:
        expression = display.get()

        if "sin" in expression:
            number = float(expression.replace("sin", ""))
            result = math.sin(math.radians(number))

        elif "cos" in expression:
            number = float(expression.replace("cos", ""))
            result = math.cos(math.radians(number))

        elif "tan" in expression:
            number = float(expression.replace("tan", ""))
            result = math.tan(math.radians(number))

        elif "cot" in expression:
            number = float(expression.replace("cot", ""))
            result = 1 / math.tan(math.radians(number))

        elif "sec" in expression:
            number = float(expression.replace("sec", ""))
            result = 1 / math.cos(math.radians(number))

        elif "cosec" in expression:
            number = float(expression.replace("cosec", ""))
            result = 1 / math.sin(math.radians(number))
        
        elif "sqrt" in expression:
            number = float(expression.replace("sqrt", ""))
            result = math.sqrt(number)

        else:
            result = eval(expression)

        display.delete(0, END)
        display.insert(0, result)

    except ZeroDivisionError:
        display.delete(0, END)
        display.insert(0, "Cannot divide by 0")

    except:
        display.delete(0, END)
        display.insert(0, "Error")
def clear():
    display.delete(0,END)
Button(root,text="7",command=seven).grid(row=1,column=0)
Button(root,text="8",command=eight).grid(row=1,column=1)
Button(root,text="9",command=nine).grid(row=1,column=2)

Button(root,text="6",command=six).grid(row=2,column=0)
Button(root,text="5",command=five).grid(row=2,column=1)
Button(root,text="4",command=four).grid(row=2,column=2)

Button(root,text="3",command=three).grid(row=3,column=0)
Button(root,text="2",command=two).grid(row=3,column=1)
Button(root,text="1",command=one).grid(row=3,column=2)

Button(root,text="0",command=zero).grid(row=4,column=1)

Button(root,text="+",command=plus).grid(row=1,column=3)
Button(root,text="-",command=minus).grid(row=2,column=3)
Button(root,text="*",command=mult).grid(row=3,column=3)
Button(root,text="/",command=divide).grid(row=4,column=3)

Button(root,text="=",command=equal).grid(row=4,column=2)
Button(root,text="C",command=clear).grid(row=4,column=0)

Button(root, text="sin", width=6, command=sin_function).grid(row=1, column=4)
Button(root, text="cos", width=6, command=cos_function).grid(row=2, column=4)
Button(root, text="tan", width=6, command=tan_function).grid(row=3, column=4)

Button(root, text="cot", width=6, command=cot_function).grid(row=1, column=5)
Button(root, text="sec", width=6, command=sec_function).grid(row=2, column=5)
Button(root, text="cosec", width=6, command=cosec_function).grid(row=3, column=5)

Button(root, text="^", width=6, command=power_function).grid(row=4, column=4)

Button(root, text="√", width=6, command=root_function).grid(row=4, column=5)
root.mainloop()


    
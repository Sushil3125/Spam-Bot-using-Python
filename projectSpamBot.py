import tkinter as tk
import pyautogui
import time 
from functools import partial

def spamming(myVar,myNum):
    time.sleep(5)
    message=myVar
    n=0
    m=int(myNum)
    while (n!=m):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        n=n+1

def call_result(label_res,var,num):
    myVar=(var.get())
    myNum=(num.get())
    label_res.config(text="Your message is : "+myVar+"\n Wait for the magic !!!!")
    spamming(myVar,myNum)
    
top=tk.Tk()
top.title("Spam Bot by Sushil Dhakal")
top.geometry('540x360')
stringVar= tk.StringVar()
NumVar=tk.StringVar()
label1=tk.Label(
    top,
    text="Enter message to Spam : ",
).grid(row=1,column=0)
entry1=tk.Entry(
    background="yellow",
    fg="black",
    textvariable=stringVar
).grid(row=2,column=0)
label2=tk.Label(
    top,
    text="Enter how many time to spam :",
).grid(row=3,column=0)
entry2=tk.Entry(
    background="yellow",
    fg="black",
    textvariable=NumVar
).grid(row=4,column=0)
label_res=tk.Label(top)
label_res.grid(row=6,column=3)
call_result=partial(call_result,label_res,stringVar,NumVar)
button_cal=tk.Button(top, text="Press to start spamming",command=call_result).grid(row=5, column=3)
top.mainloop()  

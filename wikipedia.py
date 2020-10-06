from tkinter import *
from tkinter import messagebox
import tkinter as tk
import wikipedia

def on_click():
  text.delete(1.0, END)
  q = get_q.get()
  text.insert(INSERT, wikipedia.summary(q, sentences=3))



def wrnng():
  tk.messagebox.showinfo(title='About', message='Created By Mohamed Yanis HIOU')

root = Tk()
root.title('GI Searchers')

btn = Button(root,text='About',command=wrnng)
btn.pack()

question = Label(root, text="Question")
question.pack()
get_q = Entry(root, bd =5)
get_q.pack()
submit = Button(root,text='Submit',command=on_click)
submit.pack()
text = Text(root)
text.pack()

root.mainloop()
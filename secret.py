from tkinter import *
from tkinter import messagebox
import random

def no():
      messagebox.showinfo(' ', 'я геній?')
      quit()

def motionMouse(event):
      btnn.place(x=random.randint(0, 500), y =random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('опитування')
root.resizable(width = False, height = False)
root['bg'] = 'azure'

label = Label(root, text= 'Максим геній?', font= 'Arial 20 bold', bg= 'white').pack()
btnn = Button(root, text= 'неа', font= 'Arial 20 bold')
btnn.place(x=170, y=100)
btnn.bind('<Enter>', motionMouse)

btny = Button(root, text= 'та', font= 'Arial 20 bold', command=no).place(x =350, y=100)

root.mainloop()
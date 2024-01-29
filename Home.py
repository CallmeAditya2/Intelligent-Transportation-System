import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Dashboard")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
  # , relwidth=1, relheight=1)

img=ImageTk.PhotoImage(Image.open("T.jpg"))

img2=ImageTk.PhotoImage(Image.open("T2.jpg"))

img3=ImageTk.PhotoImage(Image.open("T1.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=5)

x = 1
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image = Image.open('T2.jpg')

image = image.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

# function to change to next image
# def move():
# 	global x
# 	if x == 4:
# 		x = 1
# 	if x == 1:
# 		logo_label.config(image=img)
# 	elif x == 2:
# 		logo_label.config(image=img2)
# 	elif x == 3:
# 		logo_label.config(image=img3)
# 	x = x+1
# 	root.after(2000, move)

# # calling the function
# move()
#
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="maroon")
canvas.pack()
text_var="Traffic Prediction Using SVM"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 100
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()

# label_l1 = tk.Label(root, text="Form Based Document Using OCR Using Machine Learning",font=("Times New Roman", 35, 'bold'),
#                     background="#152238", fg="white", width=60, height=1)
# label_l1.place(x=0, y=0)



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def action():
   
    from subprocess import call
    call(["python","GUI_MASTER.py"])
    
def action1():
   
    from subprocess import call
    call(["python","Graphs.py"])
    
def action2():
   
    from subprocess import call
    call(["python","Home.py"])
    

#################################################################################################################
def window():
    root.destroy()
    
button1 = tk.Button(root, text="Traffic_Prediction",command=action, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
button1.place(x=100, y=220)
button2 = tk.Button(root, text="Data_Vizualization",command=action1, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
button2.place(x=100, y=320)


exit = tk.Button(root, text="Back", command=action2, width=16, height=1, font=('times', 20, ' bold '), bg="red",fg="white")
exit.place(x=140, y=420)

button2 = tk.Button(root, text="Exit",command=window, width=16, height=1, bg="red", fg="white",font=('times', 20, ' bold '))
button2.place(x=140, y=520)


root.mainloop()
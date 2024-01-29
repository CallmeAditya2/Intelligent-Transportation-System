from tkinter import *
import tkinter as tk
import numpy as np
import pandas as pd
#import requests
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

def Train():
    """GUI"""
    

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Traffic Prediction")
    root.configure(background="sky blue")
    Details1 = tk.IntVar()
    Details2 = tk.IntVar()
    Details3 = tk.IntVar()
    Details4 = tk.IntVar()
    Details5= tk.IntVar()
    Details6 = tk.IntVar()
    
   
    
    #===================================================================================================================
    
    
    def Detect():
        
        
        e1=Details1.get()
        print(e1)
        e2= Details2.get()
        print(e2)
        e3= Details3.get()
        print(e3)
        e4= Details4.get()
        print(e4)
        e5=Details5.get()
        print(e5)
        e6=Details6.get()
        print(e6)
        
        
        #########################################################################################
        
        from joblib import dump ,load
        a1=load('C:/Users/admin/Desktop/finalyearproject/New/Traffic Prediction/Model1.joblib')
        v= a1.predict([[e1,e2,e3,e4,e5,e6]])
        print(v)
        if v[0]==0:
            print("Route is Normal")
            yes = tk.Label(root,text="Route is Normal",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=200,y=620)
                     
        elif v[0]==1:
            print("Route is Medium")
            no = tk.Label(root, text="Route is Medium", background="orange", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=200, y=620)
            
            
        elif v[0]==2:
            print("Route is Heavy")
            #sms_send()
            no = tk.Label(root, text="Route is Heavy", background="red", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=200, y=620)
            
       
            
        
            
            
    l1=tk.Label(root,text="Source",background="olive",font=('times', 20, ' bold '),width=20)
    l1.place(x=5,y=50)
    Details1=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Details1)
    Details1.place(x=400,y=50)

    l2=tk.Label(root,text="Intermediate 1",background="olive",font=('times', 20, ' bold '),width=20)
    l2.place(x=5,y=100)
    Details2=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar= Details2)
    Details2.place(x=400,y=100)
    
    l3=tk.Label(root,text="Intermediate 2",background="olive",font=('times', 20, ' bold '),width=20)
    l3.place(x=5,y=150)
    Details3=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Details3)
    Details3.place(x=400,y=160)
    
    l4=tk.Label(root,text="Destination",background="olive",font=('times', 20, ' bold '),width=20)
    l4.place(x=5,y=200)
    Details4=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Details4)
    Details4.place(x=400,y=200)
    
    l5=tk.Label(root,text="Weather",background="olive",font=('times', 20, ' bold '),width=20)
    l5.place(x=5,y=250)
    Details5=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Details5)
    Details5.place(x=400,y=250)
  
    l6=tk.Label(root,text="Demongraphy",background="olive",font=('times', 20, ' bold '),width=20)
    l6.place(x=5,y=300)
    Details6=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Details6)
    Details6.place(x=400,y=300)
    
    

    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=500)


    root.mainloop()

Train()
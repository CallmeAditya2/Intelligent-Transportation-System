from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
import seaborn as sns 
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import accuracy_score
import warnings
import csv
warnings.filterwarnings("ignore", category=DeprecationWarning) 
root = tk.Tk()
root.title("Traffic Prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image = Image.open('T2.jpg')

image = image.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
# function to change to next image
'''def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img3)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()'''




  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Movie Prediction", font=('times', 35,' bold '), height=1, width=62,bg="brown",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    data = pd.read_csv(r"C:/Users/Sagar/Desktop/Traffic Prediction/dataset.csv")
    data.head()
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(20, 15))
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.savefig('Correlation.png', bbox_inches='tight')
    plt.show()
    
    
    
    plt.bar(data['Details6'], data['Details1'])
    plt.title('Sample Bar Chart')
    
    plt.xlabel('Details6')
    plt.ylabel('Details1')
    plt.savefig('Sample Bar Chart.png', bbox_inches='tight')
    plt.bar(data['Details6'], data['Details1'])
   
    plt.show()

# Add chart title and axis labels
    data = pd.read_csv(r"C:/Users/Sagar/Desktop/Traffic Prediction/dataset.csv")
    data.head()

    df = data.dropna()

   

    # """Feature Selection => Manual"""
    x = data.drop(['Stetus'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Stetus']
    print(type(y))
    x.shape
    
    
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    y_test = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0]
    accuracy = accuracy_score(y_test, y_pred)

    # Create data
    data = np.random.normal(accuracy, 0.1, 1000)

    # Plot histogram
    plt.hist(data, bins=30, color='blue', alpha=0.5)
    plt.axvline(x=accuracy, color='red', linestyle='--', linewidth=2)
    plt.xlabel('Accuracy')
    plt.ylabel('Frequency')
    plt.title('Histogram of Accuracy Scores')
    plt.savefig('Accuracy.png', bbox_inches='tight')
    plt.show()
    
# # Plot the accuracy as a bar graph using tkinter and matplotlib
    

#     from joblib import dump
#     dump (svcclassifier,"crime.joblib")
#     print("Model saved as crime.joblib")





# def window():
#     root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=5, y=200)



root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
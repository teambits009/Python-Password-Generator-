#Importing the required libraries for the Password Generator Project using Python 
from msilib.schema import CheckBox
import random
from tkinter import *
import string 
import tkinter 

#Checkbox - This is for creating a checkbox
#Random - This is for generating random things using random() method 
#Tkinter- This is used to create a GUI using Python
#String- This helps in accessing string literal 

#creating a window
window = Tk()
window.title ('TechOps') #window title 
window.geometry('500*500') #window geometry 

Label(window,font=('bold', 10), text= 'PASSWORD GENERATOR').pack()#giving label to window

#Here we use the Tk()method to create a window named window.We use the title() method to give title to this window and geometry()
#to give the window a specific size.Label()method is used to create a label that we are going to place on the window using the pack()method.
#We can specify the font,text,background color,etc of the label. 

#function to generate password 
# Importing the required libraries for the Password Generator Project using Python
# Function to generate password
def password_generate(length):
    valid_chars = string.ascii_letters + string.digits + '@_'
    password = ''.join(random.sample(valid_chars, length))
    label1 = Label(window, text=password, font=('bold', 20))
    label1.place(x=190, y=50)

# Example usage of the password_generate function
password_generate(12)  # You can call this function with the desired password length
#Chcekbox()method is used to create checkboxes in our windpow. We have created three checkboxes(4 character,6 characters, and 8 characters)
#We have assigned a variable name and a value to each of these checkboxes so that when a checkbox is selected it performs a desired task. The main
#concern to create a checkbox is to make sure what length of the password the user wants
#Here we have specified text, on value, offvalue and variable(variable name) for each of these checkboxes.Place()method is used to place these on the 
#window using the x and y coordination system. 

#converting string input to integer
len1=tkinter.IntVar()
len2=tkinter.IntVar()
len3=tkinter.IntVar()

#As we want to use the values on the checkboxes as integers, we will convert each checkbox variable value to integer using the IntVar()method 
#Function to check the checkbox 
def get_len():
    if len1.get() ==4:
       password_generate(4)
    elif len2.get() ==6:
        password_generate(6)
    elif len3.get() ==8:
        password_generate(8)
    else:
        password_generate(6)

#This function defines what length will be passed on to the password_generate()function 

Button(window,text='Generate' , font=('normal', 10),
bg= 'yellow', command=get_len).place (x=200, y=100)

#Using the button() method we create a button named "Generate". When we click on this button the get_len()function will get executed. We have 
#specified the background colour as yellow for the button and we place it using the place()method specifying its x and y coordinates

window.mainloop()
#run the window
mainloop()

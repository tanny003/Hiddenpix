from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb 

#headertext
root=Tk()
root.title("Steganography -Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="black")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)
def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)
def save():
    secret.save("hidden.png")

#headerlogoimage
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,background="black").place(x=200,y=0)

Label(root,text="HIDDENPIX",bg="black",fg="white",font="arial 25 bold").place(x=280,y=20)


#Frame1
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=20,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#Frame2
f2=Frame(root,bd=3,bg="white",width=310,height=280,relief=GROOVE)
f2.place(x=370,y=80)


text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)

frame3=Frame(root,bd=3,bg="black",width=340,height=100,relief=GROOVE)
frame3.place(x=20,y=370)

Button(frame3,text="Select Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=25,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=170,y=30)
Label(frame3,text="Picture,Image,Photo File",bg="black",fg="white").place(x=20,y=5)

frame4=Frame(root,bd=3,bg="black",width=320,height=100,relief=GROOVE)
frame4.place(x=370,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=25,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=170,y=30)
Label(frame4,text="Picture,Image,Photo File",bg="black",fg="white").place(x=20,y=5)




root.mainloop()
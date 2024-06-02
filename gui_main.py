from tkinter import * 
import tkinter  as tk  #Tkinter used for GUI Part. Created object as tk
from PIL import Image , ImageTk  #Pillow Library for using images

root = tk.Tk() #created New window using Tk() and stored it into variable root  
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


#title
root.title("Bird Species Identification")



#-------function------------------------

def reg():
# tkinter window 
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
# tkinter window 
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])    #subprocess call() function returns the executed code of the program
    


#For background Image
image2 =Image.open('bird1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS) #Antialias for showing clear images

background_image=ImageTk.PhotoImage(image2)  # Tkinter PhotoImage used to display an image for a Label

background_label = tk.Label(root, image=background_image)

background_label.place(x=0, y=0) # relwidth=1, relheight=1)


lbl = tk.Label(root, text="Bird Species Identification", font=('times', 40,' bold '), height=1, width=50,bg="#000000",fg="white")
lbl.place(x=0, y=0)

#Frame
framed = tk.LabelFrame(root, text="WELCOME", width=500, height=250, bd=20, font=('times', 24, ' bold '),bg="pink")
#framed.grid(row=0, column=0)
framed.place(x=550, y=270)


#Login Button
button1 = tk.Button(framed, text='Login Now',width=17,height=2,bd=10,bg='green',fg='black',command=login,font='bold').place(x=15,y=45)

#Register button
button1 = tk.Button(framed, text='Register',width=17,height=2,bd=10,bg='green',fg='black',command=reg,font='bold').place(x=230,y=45)


root.mainloop() #when we want to run our application
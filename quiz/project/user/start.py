from tkinter import*
from tkinter import messagebox  #use tu show enter your passowrd and your name etc.
from PIL import Image, ImageTk
import userLogin



class Labelwindow:
    def __init__(self):
        self.root=Tk()  # create GUI
        self.root.title (" QUIZ HUB ")
        self.root.config(bg="black")
        self.root.geometry('700x600+400+100')
        # Show image using label
        self.image = ImageTk.PhotoImage(Image.open('photos/start.jpeg').resize((700, 600)))
        self.label1 = Label(self.root, image = self.image)
        self.label1.place(x=0,y=-5)
       
        #entry_points
        
        #Button
        Button(self.root,text="start →",command=self.openpage,bg="orange",bd=5,fg="black",width=7,font="italic 15").place(x=300,y=540)
        self.root.mainloop() 
    
            
if __name__=="__main__":
    obj= Labelwindow()
    
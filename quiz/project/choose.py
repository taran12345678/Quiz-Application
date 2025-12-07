from tkinter import*
from tkinter import messagebox  #use tu show enter your passowrd and your name etc.
from PIL import Image, ImageTk

import login



class Labelwindow:
    def __init__(self):
        self.root=Tk()  # create GUI
        self.root.title (" QUIZ HUB ")
        self.root.config(bg="black")
        self.root.geometry('700x600+400+100')
        # Show image using label
       #elf.label1.place(x=0,y=-5)
        #show quiz hub
        #Label(self.root, text="Quiz Hub",font="none 60 italic ",fg='orange',bg="black",bd=0).place(x=85, y=30)
        
        # fetch imformation

        #Label(self.root,text="username :",fg="white",bg="black",font="calibri 26 ").place(x=84,y=175)
       # Label(self.root,text="password :",fg="white",bg="black",font="calibri 26 ").place(x=87,y=220)
        
        #entry_points
        #self.entry1=Entry(self.root,bd=5,width=25)  # use create box to fill details
        #self.entry1.place(x=250,y=190)
        #self.entry2=Entry(self.root,bd=5,show="*",width=25)
        #self.entry2.place(x=250,y=235)
        
        #Button
        Button(self.root,text="ADMIN",command=self.openpage2,bg="orange",bd=5,fg="black",width=7,font="italic 15").place(x=180,y=250)
        Button(self.root,text="USER",command=self.openpage1,bg="orange",bd=5,fg="black",width=7,font="italic 15").place(x=400,y=250)
        self.root.mainloop()
        
        
    def openpage1(self):
      self.root.destroy()
      obj = user.userlogin.Labelwindow()
      obj.menus()
    def openpage2(self):
      self.root.destroy()
      obj = login.Labelwindow()
      obj.menus()
    

    
        
        
if __name__=="__main__":
    obj= Labelwindow()
    

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import userDatabase, openTopic
import os

class Labelwindow:
  def __init__(self, res):

    self.userRes = res

    self.root=Toplevel()
    self.root.title(' QUIZ HUB ')
    self.root.config(bg="black")
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('700x600+400+100')
    
    
    Label(self.root, text="Select subject ",font="none 40 italic ",fg='white',bg="black").place(x=200, y=130)

    self.frame = Frame(self.root, bg='white', padx=20, pady=20)
    self.frame.place(x = 0, y = 200, width=700, height='600')
    #self.image = ImageTk.PhotoImage(Image.open("0..jpg").resize((700, 600)))
    #self.label1 = Label(self.root, image = self.image)
    #self.label1.place(x=0,y=-5)
    


    res = userDatabase.getSubjects()
    if res:
      row = 0
      col = 0
      for i in res:
        self.subBtn = Button(self.frame, text=i[1] , padx=20, pady=20, command=lambda x = i[0]: self.openTopic(x))
        self.subBtn.grid(row=row, column=col, padx=10)
        col += 1
    else:
      messagebox.showerror()
    

    self.root.mainloop()


  def openTopic(self, x):
    # print(x)
    self.root.destroy()
    obj = openTopic.openTopics(x, self.userRes)




if __name__=="__main__":
  obj= Labelwindow()
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel=Label(self,text='hello,world')
        # self.helloLabel.pack()
        # self.quitButton=Button(self,text='Quit',command=self.quit)
        # self.quitButton.pack()
        self.nameIput=Entry(self)
        self.nameIput.pack()
        self.alertButton=Button(self,text='enter',command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name=self.nameIput.get()or 'world'
        messagebox.showinfo('message','hello,%s'%name)

app=Application()
app.master.title('hello world')
app.mainloop()
print(app.mainloop())
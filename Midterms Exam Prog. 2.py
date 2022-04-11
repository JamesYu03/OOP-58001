from tkinter import *
class Name:
    def __init__(self, name):
        self.lbl1=Label(name, text='Enter your full name', fg="red")
        self.lbl1.place(x=50, y=30)

        self.t1 = Entry(bd=3)
        self.t1.place(x=300, y=25)
        self.t2 = Entry(bd=3)
        self.t2.place(x=300, y=100)

        self.btn1 = Button(name, text='Click to display your full name', fg = "red")
        self.btn1 = Button(name, text='Click to display your full name', fg = "red", command=self.display)
        self.btn1.place(x=50, y=100)

    def display(self):
        fname=str(self.t1.get())
        result= fname
        self.t2.insert(END, str(result))



window=Tk()
myname=Name(window)
window.title('TEMPERATURE UNIT CONVERTION')
window.geometry("550x300+10+10")
window.mainloop()
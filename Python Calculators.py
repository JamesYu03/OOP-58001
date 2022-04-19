from tkinter import *
window = Tk()
window.title('Simple Calculator')
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.place(relx=0.50, rely=0.10, anchor="center")

        self.lbl2 = Label (window, text="Input 1st Number: ")
        self.lbl2.place(x=40, y=60)
        self.t1 = Entry(window, bd=3)
        self.t1.place(x=150,y=60)

        self.lbl3 = Label(window, text="Input 2nd Number: ")
        self.lbl3.place(x=40, y=100)
        self.t2 = Entry(window, bd=3)
        self.t2.place(x=150, y=100)

        self.lbl4 = Label(window, text="Choose among the operators")
        self.lbl4.place(x=110, y=135)

        self.btn1 = Button(window, text='Add(+)')
        self.btn1 = Button(window, text='Add(+)', command=self.add)
        self.btn1.place(x=40, y=170)

        self.btn2 = Button(window, text='Subtract(-)')
        self.btn2 = Button(window, text='Subtract(-)', command=self.sub)
        self.btn2.place(x=100, y=170)

        self.btn3 = Button(window, text='Multiply(*)')
        self.btn3 = Button(window, text='Multiply(*)', command=self.mul)
        self.btn3.place(x=180, y=170)

        self.btn4 = Button(window, text='Divide(/)')
        self.btn4 = Button(window, text='Divide(/)', command=self.div)
        self.btn4.place(x=260, y=170)

        self.lbl5 = Label(window, text="Result")
        self.lbl5.place(x=40, y=220)
        self.t3 = Entry(window, bd=3)
        self.t3.place(x=120, y=220)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = (num1+num2)
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = (num1+num2)
        self.t3.insert(END, str(result))

    def mul(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = (num1*num2)
        self.t3.insert(END, str(result))

    def div(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = (num1/num2)
        self.t3.insert(END, str(result))


mywin=MyWindow(window)

window.mainloop()



from tkinter import *
class TemperatureConversion:
    def __init__(self, temp):
        self.lbl1=Label(temp, text='Enter Temperature')
        self.lbl1.place(x=50, y=25)
        self.lbl2 = Label(temp, text='Result')
        self.lbl2.place(x=50, y=200)

        self.t1 = Entry(bd=3)
        self.t1.place(x=160, y=25)
        self.t2 = Entry(bd=3)
        self.t2.place(x=160, y=200)

        self.btn1 = Button(temp, text='Fahrenheit to Celsius')
        self.btn1 = Button(temp, text='Fahrenheit to Celsius', command=self.FtC)
        self.btn1.place(x=50, y=100)

        self.btn2 = Button(temp, text='Kelvin to Celsius')
        self.btn2 = Button(temp, text='Kelvin to Celsius', command=self.KtC)
        self.btn2.place(x=230, y=100)

    def FtC(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result=(num1-32)*5/9
        self.t2.insert(END, str(result))

    def KtC(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result=(num1-273.15)
        self.t2.insert(END, str(result))


window=Tk()
mytemp=TemperatureConversion(window)
window.title('TEMPERATURE UNIT CONVERTION')
window.geometry("400x300+10+10")
window.mainloop()
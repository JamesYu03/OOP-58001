from tkinter import *
window = Tk()
window.title("Finding Smallest Number")
window.geometry("550x350+20+100")
def findSmallest():
    L = []
    L.append(eval(Num1.get()))
    L.append(eval(Num2.get()))
    L.append(eval(Num3.get()))
    LNum.set(min(L))

#labels
lbl1 = Label(window, text = "Find the least number among three numbers",justify='center')
lbl1.grid(row=0, column=1,pady=5)

lbl2 = Label(window,text = "Enter the first number:")
lbl2.grid(row=1, column = 0,sticky=W,pady=5, padx=5)

lbl3 = Label(window,text = "Enter the second number:")
lbl3.grid(row=2, column=0, pady=5, padx=5)

lbl4 = Label(window,text="Enter the third number:")
lbl4.grid(row=3,column =0, sticky=W, pady=5, padx=5)

lbl5 = Label(window,text="The smallest number:")
lbl5.grid(row=5,column=0,sticky=W, pady=5, padx=5)

#entry
Num1 = StringVar()
entr1 = Entry(window,bd=3,textvariable=Num1)
entr1.grid(row=1, column = 1, pady=5, padx=5)

Num2=StringVar()
entr2 = Entry(window,bd=3,textvariable=Num2)
entr2.grid(row=2,column=1, pady=5, padx=5)

Num3 = StringVar()
entr3 = Entry(window,bd=3,textvariable=Num3)
entr3.grid(row=3, column=1, pady=5, padx=5)

LNum = StringVar()
entr4 = Entry(window,bd=3,state="readonly",textvariable=LNum)
entr4.grid(row=5,column=1, pady=5, padx=5)

#button

btn1 = Button(window,text = "The smallest number among the three is:",command=findSmallest)
btn1.grid(row=4, column = 1, pady=5, padx=5)



mainloop()
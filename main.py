from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("500x300+10+20")
window.title("Main GUI")

button=Button(window,text = "Button", fg = "red", font =("Verdana",16))
button.place(x=50,y=70)

label=Label(window,text = "This is a label", fg= "blue", bg = "orange")
label.place(x=100,y=170)

txtfld = Entry(window,text = "This is a text field", bd = 5)
txtfld.place(x=210,y=170)

v1=IntVar()
radiobutton = Radiobutton(window,text = "Male",variable=v1,value = 1)
radiobutton1 = Radiobutton(window,text = "Female",variable=v1,value = 2)
radiobutton.place(x=30, y=40)
radiobutton1.place(x=30)

v2=StringVar()
v2.set('Student1')
data1 = "Student1","Student2","Student3"
combo = ttk.Combobox(window,values=data1)
combo.place(x=360)

data = "Student1","Student2","Student3"
lb = Listbox(window, height =5, selectmode="single")
for num in data:
    lb.insert(END, num)
lb.place(x=210)
window.mainloop()

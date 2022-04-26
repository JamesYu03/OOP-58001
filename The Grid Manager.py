from tkinter import *
window = Tk()
window.geometry("400x300+20+10")
window.title("The Grid Manager")

Ent1 = Entry(window, bd=2, justify="center", fg="blue")
Ent1.grid(row=0, column=0)
Ent1.insert(0, "row 0, column 0")

Ent2 = Entry(window, bd=2, justify="center", fg="blue")
Ent2.grid(row=0, column=1)
Ent2.insert(0, "row 0, column 1")

Ent3 = Entry(window, bd=2, justify="center", fg="blue")
Ent3.grid(row=0, column=2)
Ent3.insert(0, "row 0, column 2")

Ent4 = Entry(window, bd=2, justify="center", fg="red")
Ent4.grid(row=1, column=0)
Ent4.insert(0, "row 1, column 0")

Ent5 = Entry(window, bd=2, justify="center", fg="red")
Ent5.grid(row=1, column=1)
Ent5.insert(0, "row 1, column 1")

Ent6 = Entry(window, bd=2, justify="center", fg="red")
Ent6.grid(row=1, column=2)
Ent6.insert(0, "row 1, column 2")

Ent7 = Entry(window, bd=2, justify="center", fg="green")
Ent7.grid(row=2, column=0)
Ent7.insert(0, "row 2, column 0")

Ent8 = Entry(window, bd=2, justify="center", fg="green")
Ent8.grid(row=2, column=1)
Ent8.insert(0, "row 2, column 1")

Ent9 = Entry(window, bd=2, justify="center", fg="green")
Ent9.grid(row=2, column=2)
Ent9.insert(0, "row 2, column 2")


yscroll = Scrollbar(window, orient='vertical')
yscroll.grid(row=5, column=2, rowspan=4, padx=(0,100), pady=5, sticky=NS)


datalist = ["Student1", "Student2", "Student3", "Student4", "Student5", "Student6", "Student7", "Student8", "Student9", "Student10"
            , "Student11", "Student12", "Student13", "Student14", "Student15"]
var = StringVar()

lb = Listbox(window, listvariable=var, yscrollcommand=yscroll.set, width=10, height=4)
lb.grid(row=5, column=1)
var.set(tuple(datalist))
yscroll["command"]= lb.yview()



window.mainloop()

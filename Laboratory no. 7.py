from tkinter import *
number = "" # globally declare the expression variable
                # Function to update expression
                # in the text entry box
def press(num):
    # point out the global expression variable
    global number
    # concatenation of string
    number = number + str(num)
    # update the expression by using set method
    equation.set(number)
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
    # Put that code inside the try block
    # which may generate the error
    try:
        global number
        # eval function evaluate the expression
        # and str function convert the result
        # into string

        total = str(eval(number))
        equation.set(total)
        # initialize the expression variable
        # by empty string
        number = ""
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" Syntax Error ")
        number = ""
# Function to clear the contents
# of text entry box
def clear():
    global number
    number = ""
    equation.set("")

if __name__ == "__main__":
    window = Tk()
window.geometry("385x500+20+50")
window.title("Calculator")
window.configure(background='#A5BFDA')

equation = StringVar()

number_field = Entry(window, font=('Helvetica 16 bold'), textvariable=equation, bg='#B0E0E6',bd=20)
number_field.grid(row=0, column=0, columnspan=10, ipadx=50, ipady=8)
clr = Button(text="C", justify="center",font=('Helvetica 15 bold'), command=clear)
clr.grid(row=1, column=0, columnspan=12, sticky= W, ipadx=174, ipady=10, pady=2, padx=2)
        #top row
no7 = Button(text="7", font=('Helvetica 15 bold'), width=7, height=2, command=lambda: press(7))
no7.grid(row=2, column=0, columnspan=3, padx=1,pady=3, sticky=W)

no8 = Button(text="8", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(8))
no8.grid(row=2, column=3, columnspan=3, padx=1, sticky=W)

no9 = Button(text="9", font=('Helvetica 15 bold'),width=7, height=2,command=lambda: press(9))
no9.grid(row=2, column=6, columnspan=3, padx=1)

div = Button(text="/", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press("/"))
div.grid(row=2, column=9,columnspan=3, padx=1, sticky=W)
        #middle row
no4 = Button(text="4",  font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(4))
no4.grid(row=3, column=0, columnspan=3, pady=3)

no5 = Button(text="5", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(5))
no5.grid(row=3, column=3, columnspan=3)

no6 = Button(text="6", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(6))
no6.grid(row=3, column=6, columnspan=3)

mul = Button(text="*", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press("*"))
mul.grid(row=3, column=9, columnspan=3)
        #bottom row
no1 = Button(text="1", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(1))
no1.grid(row=4, column=0, columnspan=3)

no2 = Button(text="2",font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(2))
no2.grid(row=4, column=3, columnspan=3)

no3 = Button(text="3", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press(3))
no3.grid(row=4, column=6, columnspan=3)

min = Button(text="-", font=('Helvetica 15 bold'),width=7, height=2, command=lambda: press("-"))
min.grid(row=4, column=9, columnspan=3)

        #0, decimal point and plus
no0 = Button(text="0", font=('Helvetica 15 bold'), command=lambda: press(0))
no0.grid(row=5, column=0, columnspan=4,ipadx=50, ipady=10, pady=3)

dec = Button(text=".",font=('Helvetica 15 bold'), command=lambda: press("."))
dec.grid(row=5, column=4, columnspan=4,ipadx=50, ipady=10)

plu = Button(text="+",font=('Helvetica 15 bold'), command=lambda: press("+"))
plu.grid(row=5, column=8, columnspan=4,ipadx=50,ipady=10)

        #equal sign
equal= Button(text="=", font=('Helvetica 15 bold'),command=equalpress)
equal.grid(row=6, column=0, columnspan=12, ipadx=175, ipady=10, pady=2, padx=2)




window.mainloop()

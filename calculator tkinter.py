from tkinter import *
cal = Tk()
cal.title(" Calculator ")
cal.config(bg = "black")
#cal.resizable(False,False)

name1 = Entry(cal, textvariable="nameValue",width=30 ,bd=2,font=20)
name1.grid(row = 1, column = 0,columnspan = 30, padx = 10,pady = 10)
def click(n):              #n is no. which is clicked
    curr = name1.get()
    name1.delete(0, END)
    name1.insert(0,str(curr + n))

def clr():
    name1.delete(0,END)

def add():
    a = name1.get()
    global fn  #fn means first entered no.
    global math
    math = "add"
    fn = int(a)
    name1.delete(0,END)
    
def sub():
    a = name1.get()
    global fn  #fn means first entered no.
    global math
    math = "sub"
    fn = int(a)
    name1.delete(0,END)

def mul():
    a = name1.get()
    global fn  #fn means first entered no.
    global math
    math = "mul"
    fn = int(a)
    name1.delete(0,END)

def div():
    a = name1.get()
    global fn  #fn means first entered no.
    global math
    math = "div"
    fn = int(a)
    name1.delete(0,END)
    
def equal():
    sn = name1.get()   #sn means Second entered no.
    name1.delete(0,END)
    if math == "add":
        name1.insert(0, fn + int(sn))
    elif math == "sub":
        name1.insert(0, fn - int(sn))
    elif math == "mul":
        name1.insert(0, fn * int(sn))
    else:
        name1.insert(0, fn / int(sn))
    
b7 = Button(cal, text = "7" ,padx = 40,bg='black',fg='white',pady = 20,font = "Times 18", command = lambda: click("7"))
b8 = Button(cal, text = "8" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("8"))
b9 = Button(cal, text = "9" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("9"))
b4 = Button(cal, text = "4" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("4"))
b5 = Button(cal, text = "5" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("5"))
b6 = Button(cal, text = "6" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("6"))
b2 = Button(cal, text = "1" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("1"))
b3 = Button(cal, text = "2" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("2"))
b0 = Button(cal, text = "0" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("0"))
b1 = Button(cal, text = "3" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = lambda: click("3"))
bpl = Button(cal, text = "+" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = add)
bmi = Button(cal, text = "__" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = sub)
bmu = Button(cal, text = "X" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = mul)
bdi = Button(cal, text = "/" ,padx = 40,bg='black',pady = 20,fg='white',font = "Times 18", command = div)
br = Button(cal, text = "C" ,padx = 40,bg='orange',pady = 20,fg='black',font = "Times 18", command = clr)
beq = Button(cal, text = "=" ,padx = 40,bg='red',pady = 20,fg='black',font = "Times 18", command = equal)


b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)
b4.grid(row = 3, column = 0)
b5.grid(row = 3, column = 1)
b6.grid(row = 3, column = 2)
b2.grid(row = 4, column = 0)
b3.grid(row = 4, column = 1)
b0.grid(row = 5, column = 1)
b1.grid(row = 4, column = 2)
bpl.grid(row = 5, column = 3)
bmi.grid(row = 4, column = 3)
bmu.grid(row = 3, column = 3)
bdi.grid(row = 2, column = 3)
br.grid(row = 5, column = 0 )
beq.grid(row = 5, column = 2 )



cal.mainloop()  # or  ===>  mainloop() 

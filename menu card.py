from tkinter import *
win = Tk()
win.title(" Menu Card ")
win.geometry("1400x760")
win.resizable(False,False)
 # Labeling to display food items names
label = Label(win, text=" **HOTEL ASWAD**",fg="red",bg="yellow",font="arial 36")
label.place(x = 90,y = 30)

#labels of menu card
label = Label(win, text=" Menu ",fg="brown",bg="sky blue",font="arial 32")
label.place(x = 920,y = 30)

label = Label(win, text="Nasta :",fg="brown",bg="yellow",font="arial 27")
label.place(x = 850,y = 110)

label = Label(win, text="Veg Recipe :",fg="brown",bg="yellow",font="arial 27")
label.place(x = 850,y = 430)

l1 = Label(win, text="Pav Bhaji       ...... 70",fg='brown',font="arial 25")
l1.place(x = 850,y = 160)

l2 = Label(win, text="Dosa             ...... 60",fg='brown',font="arial 25")
l2.place(x = 850,y = 220)

l3 = Label(win, text="Uttapam          ...... 70",fg='brown',font="arial 25")
l3.place(x = 850,y = 280)

l4 = Label(win, text="Idli Sambhar    ...... 70",fg='brown',font="arial 25")
l4.place(x = 850,y = 340)

l5 = Label(win, text="Kolhapuri Thali       .... 150",fg='brown',font="arial 25")
l5.place(x = 850,y = 480)

l6 = Label(win, text="Maharashtrian Thali   .... 200",fg='brown',font="arial 25")
l6.place(x = 850,y = 540)

l7 = Label(win, text="Aloo Paratha          .... 130",fg='brown',font="arial 25")
l7.place(x = 850,y = 600)

def cal():
    pb = name1.get()
    ds = name2.get()
    ut = name3.get()
    il = name4.get()
    kt = name5.get()
    mt = name6.get()
    ap = name7.get()
    total=(int(pb)*70)+(int(ds)*80)+(int(ut)*70)+(int(il)*60)+(int(kt)*150)+(int(mt)*200)+(int(ap)*130)
    ltotal = Label(win,text = total,bg='skyblue',fg='black',font="arial 22")
    ltotal.place(x = 600,y = 300)
     
label1 = Label(win, text="Pav Bhaji ...... ",fg="black",font="arial 22")
label1.place(x = 10,y = 160)

label2 = Label(win, text="Dosa ...... ",fg="black",font="arial 25")
label2.place(x = 10,y = 230)

label3 = Label(win, text="Uttapam ......",fg="black",font="arial 22")
label3.place(x = 10,y = 300)

label4 = Label(win, text="Idli Sambhar ...... ",fg="black",font="arial 22")
label4.place(x = 10,y = 370)

label5 = Label(win, text="Kolhapuri Thali .... ",fg="black",font="arial 22")
label5.place(x = 10,y = 510)

label6 = Label(win, text="Maharashtrian Thali .... ",fg="black",font="arial 22")
label6.place(x = 10,y = 580)

label7 = Label(win, text="Aloo Paratha ....",fg="black",font="arial 22")
label7.place(x = 10,y = 650)

# Entry fields for taking input

name1 = Entry(win, textvariable="nameValue",width=12 ,bd=2,font=20)
#name1.grid(padx = 100,pady = 750)  we can give .grid as well as .place for entry field ,slight diff. in x& y locality

name1.place(x = 350,y = 160)
#insert(0,"") or insert(0,int) is used for giving the default value of entry field.

name1.insert(0,0) 

name2 = Entry(win, textvariable="name2Value",width=12 ,bd=2,font=20)
name2.place(x = 350,y = 230)
name2.insert(0,0)

name3 = Entry(win, textvariable="name3Value",width=12 ,bd=2,font=20)
name3.place(x = 350,y = 300)
name3.insert(0,0)

name4 = Entry(win, textvariable="name4Value",width=12 ,bd=2,font=20)
name4.place(x = 350,y = 380)
name4.insert(0,0)

name5 = Entry(win, textvariable="name5Value",width=12 ,bd=2,font=20)
name5.place(x = 350,y = 510)
name5.insert(0,0)

name6 = Entry(win, textvariable="name6Value",width=12 ,bd=2,font=20)
name6.place(x = 350,y = 585)
name6.insert(0,0)

name7 = Entry(win, textvariable="name7Value",width=12 ,bd=2,font=20)
name7.place(x = 350,y = 660)
name7.insert(0,0)

b1 = Button(win, text = " Total" ,padx = 30,pady = 10,font="arial 10", command = cal)
b1.place(x = 580,y = 230)
#win.update()

mainloop()


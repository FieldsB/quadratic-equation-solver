from tkinter import*
def rozv():
    a=int(txt1.get())
    b=int(txt2.get())
    c=int(txt3.get())
    d = b*b-4*a*c
    
    if d>0:
        x1=(-b-d**(1/2))/2*a
        x2=(-b+d**(1/2))/2*a
        r = str(int(x1*100)/100)+ '        ' + str(int(x2*100)/100)
        lbl4.configure( text=r)
    elif d == 0:
        x=-b/2*a
        r = str(x)
        lbl4.configure( text=r)
    else:
        lbl4.configure( text='не має розвязків')
windows=Tk()
windows.title('Квадратне рівняння')

lbl1=Label(windows,text='a')
lbl1.grid(column=0, row=0)

txt1=Entry(windows, width=10)
txt1.grid(column=1, row=0)

lbl2=Label(windows,text='b')
lbl2.grid(column=2, row=0)

txt2=Entry(windows, width=10)
txt2.grid(column=3, row=0)

lbl3=Label(windows,text='с')
lbl3.grid(column=4, row=0)

txt3=Entry(windows, width=10)
txt3.grid(column=5, row=0)

btn=Button(windows, command=rozv, width = 10, text = "Виконати")
btn.grid(column=1, row=1)

lbl4 = Label(windows, text = '')
lbl4.grid(column = 2, row = 1)

windows.mainloop()
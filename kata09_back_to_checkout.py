#kata09-Back to the checkout http://codekata.com/kata/kata09-back-to-the-checkout/
from Tkinter import *

root = Tk()
root.geometry("1600x800")
root.title("Super market Pricing")

def dec1():
    pass
def inc1():
    pass
def dec2():
    pass
def inc2():
    pass
def dec3():
    exit()
def inc3():
    pass
def dec4():
    exit()
def inc4():
    pass
def reset():
    A.set("0")
    B.set("0")
    C.set("0")
    D.set("0")
def qExit():
    root.destroy()
def Total():
    pass

A=StringVar()
B=StringVar()
C=StringVar()
D=StringVar()

Tops =Frame(root,width=1600,height=200,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=800,relief=SUNKEN)
f1.pack(side=TOP)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=BOTTOM)
text_Input = StringVar

lblInfo=Label(Tops, font=('arial',50,'bold'),text="Super Market Pricing",fg="steel blue", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input,insertwidth=1,bd=10,bg="white",justify='left')
txtDisplay.grid(row=8,column=2)

lblA = Label(f1,font=('arial',16,'bold'),text="A",bd=10,anchor='w')
lblA.grid(row=0,column=0)
btndec1=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="-",bg='white',command=dec1).grid(row=0,column=1)
txtA=Entry(f1,font=('arial',11,'bold'),textvariable=A, insertwidth=1,bd=10,justify='right')
txtA.grid(row=0,column=2)
btninc1=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="+",bg='white',command=inc1).grid(row=0,column=3)

lblB = Label(f1,font=('arial',16,'bold'),text="B",bd=16,anchor='w')
lblB.grid(row=1,column=0)
btndec2=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="-",bg='white',command=dec2).grid(row=1,column=1)
txtB=Entry(f1,font=('arial',11,'bold'),textvariable=B, insertwidth=1,bd=10,justify='right')
txtB.grid(row=1,column=2)
btninc2=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="+",bg='white',command=inc2).grid(row=1,column=3)

lblC = Label(f1,font=('arial',16,'bold'),text="C",bd=16,anchor='w')
lblC.grid(row=2,column=0)
btndec3=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="-",bg='white',command=dec3).grid(row=2,column=1)
txtC=Entry(f1,font=('arial',11,'bold'),textvariable=C, insertwidth=1,bd=10,justify='right')
txtC.grid(row=2,column=2)
btninc3=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="+",bg='white',command=inc3).grid(row=2,column=3)

lblD = Label(f1,font=('arial',16,'bold'),text="D",bd=16,anchor='w')
lblD.grid(row=3,column=0)
btndec4=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="-",bg='white',command=dec4).grid(row=3,column=1)
txtD=Entry(f1,font=('arial',11,'bold'),textvariable=D, insertwidth=1,bd=10,justify='right')
txtD.grid(row=3,column=2)
btninc4=Button(f1,fg='black',font=('arial',11,'bold'),width=3,text="+",bg='white',command=inc4).grid(row=3,column=3)

btnTotal=Button(f1,padx=16,pady=8,bd=3,fg='black',font=('arial',16,'bold'),width=3,text="Total", bg='white',command=Total).grid(row=5,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=3,fg='black',font=('arial',16,'bold'),width=3,text="Reset", bg='white',command=reset).grid(row=5,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=3,fg='black',font=('arial',16,'bold'),width=3,text="Exit", bg='white',command=qExit).grid(row=5,column=3)

root.mainloop()

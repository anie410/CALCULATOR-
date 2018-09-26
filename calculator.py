from tkinter import *

def btnClick(n):
    global operator
    operator= operator+str(n)
    text_inp.set(operator)
def btnclear():
    global operator
    operator=""
    text_inp.set("")

def btnequal():
    global operator
    res=str(eval(operator))
    text_inp.set(res)
    operator=""
                    


cal=Tk()
cal.title("calculator")
operator=""
text_inp = StringVar()

txtDisplay=Entry(cal,font=('arial', 20,'bold'),textvariable = text_inp
,bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)

btn7=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="7",command=lambda:btnClick(7))

btn7.grid(row=1,column=0)

btn8=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="8",command=lambda:btnClick(8))

btn8.grid(row=1,column=1)

btn9=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="9",command=lambda:btnClick(9))

btn9.grid(row=1,column=2)

btnAdd=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="+",command=lambda:btnClick("+"))

btnAdd.grid(row=1,column=3)

btn4=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="4",command=lambda:btnClick(4))

btn4.grid(row=2,column=0)

btn5=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="5",command=lambda:btnClick(5))

btn5.grid(row=2,column=1)

btn6=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="6",command=lambda:btnClick(6))

btn6.grid(row=2,column=2)

btnSub=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="-",command=lambda:btnClick("-"))

btnSub.grid(row=2,column=3)

btn1=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="1",command=lambda:btnClick(1))

btn1.grid(row=3,column=0)

btn2=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="2",command=lambda:btnClick(2))

btn2.grid(row=3,column=1)

btn3=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="3",command=lambda:btnClick(3))

btn3.grid(row=3,column=2)

btnMul=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="*",command=lambda:btnClick("*"))

btnMul.grid(row=3,column=3)

btn0=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="0",command=lambda:btnClick(0))

btn0.grid(row=4,column=0)

btnClr=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="C",command=btnclear)

btnClr.grid(row=4,column=1)

btnEq=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="=",command=btnequal)

btnEq.grid(row=4,column=2)

btndiv=Button(cal , padx=16,pady=16 ,bd=8 ,fg="black" ,font=('arial' ,20,'bold'), text="/",command=lambda:btnClick("/"))

btndiv.grid(row=4,column=3)





cal.mainloop()

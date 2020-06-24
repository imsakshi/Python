import tkinter

root = tkinter.Tk()
res = ""


def btn1_click():
    global res
    res = res + "1"
    vardisplay.set(res)


def btn2_click():
    global res
    res = res + "2"
    vardisplay.set(res)
    return res


def btn3_click():
    global res
    res = res + "3"
    vardisplay.set(res)
    return res


def btn4_click():
    global res
    res = res + "4"
    vardisplay.set(res)
    return res


def btn5_click():
    global res
    res = res + "5"
    vardisplay.set(res)
    return res


def btn6_click():
    global res
    res = res + "6"
    vardisplay.set(res)
    return res


def btn7_click():
    global res
    res = res + "7"
    vardisplay.set(res)
    return res


def btn8_click():
    global res
    res = res + "8"
    vardisplay.set(res)
    return res


def btn9_click():
    global res
    res = res + "9"
    vardisplay.set(res)
    return res


def btn0_click():
    global res
    res = res + "0"
    vardisplay.set(res)
    return res


def btnadd_click():
    global res
    res = res + "+"
    vardisplay.set(res)
    return res


def btnsub_click():
    global res
    res = res + "-"
    vardisplay.set(res)
    return res


def btndivide_click():
    global res
    res = res + "/"
    vardisplay.set(res)
    return res


def btnmul_click():
    global res
    res = res + "*"
    vardisplay.set(res)
    return res


def btnequal_click():
    global res
    x = str(eval(res))

    res = res + "=" + x
    vardisplay.set(res)
    res = ""


root.minsize(width=300, height=300)

vardisplay = tkinter.IntVar()
textdisplay = tkinter.Entry(root, text="", width=34, textvariable=vardisplay)
textdisplay.grid(row=0, column=0, columnspan=6)

btn1 = tkinter.Button(root, text="1", width=6, command=btn1_click)
btn1.grid(row=1, column=0)

btn2 = tkinter.Button(root, text="2", width=6, command=btn2_click)
btn2.grid(row=1, column=1)

btn3 = tkinter.Button(root, text="3", width=6, command=btn3_click)
btn3.grid(row=1, column=2)

btn4 = tkinter.Button(root, text="4", width=6, command=btn4_click)
btn4.grid(row=2, column=0)

btn5 = tkinter.Button(root, text="5", width=6, command=btn5_click)
btn5.grid(row=2, column=1)

btn6 = tkinter.Button(root, text="6", width=6, command=btn6_click)
btn6.grid(row=2, column=2)

btn7 = tkinter.Button(root, text="7", width=6, command=btn7_click)
btn7.grid(row=3, column=0)

btn8 = tkinter.Button(root, text="8", width=6, command=btn8_click)
btn8.grid(row=3, column=1)

btn9 = tkinter.Button(root, text="9", width=6, command=btn9_click)
btn9.grid(row=3, column=2)

btn0 = tkinter.Button(root, text="0", width=6, command=btn0_click)
btn0.grid(row=4, column=1)

btnadd = tkinter.Button(root, text="+", width=6, command=btnadd_click)
btnadd.grid(row=1, column=3)

btnsub = tkinter.Button(root, text="-", width=6, command=btnsub_click)
btnsub.grid(row=2, column=3)

btndivide = tkinter.Button(root, text="/", width=6, command=btndivide_click)
btndivide.grid(row=3, column=3)

btnmul = tkinter.Button(root, text="X", width=6, command=btnmul_click)
btnmul.grid(row=4, column=3)

btnequal = tkinter.Button(root, text="=", width=6, command=btnequal_click)
btnequal.grid(row=4, column=2)

root.mainloop()

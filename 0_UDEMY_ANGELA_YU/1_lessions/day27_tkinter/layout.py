import tkinter

layout = tkinter.Tk()
layout.minsize(width=500,height=300)
layout.title(string="My First GUI Program")


label = tkinter.Label(text="New Text", font=("Arial", 20,"bold"))
label.grid(column=0,row=0)

button1 = tkinter.Button(text='Button')
button1.grid(column=2,row=0)

button2 = tkinter.Button(text="Button2")
button2.grid(column=1,row=1)

input = tkinter.Entry(width=10)
input.get()
input.grid(column=3,row=2)






layout.mainloop()
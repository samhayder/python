import tkinter

windows = tkinter.Tk()
windows.title("My first Tkinter package.")
windows.minsize(width=600,height=300)

# Label
my_label = tkinter.Label(text="I am a Label text.", font=("Arail",24))
my_label.pack()

# Button
def change_label_text():
    input_text = my_input.get()
    # my_label.config(text="Change Label")
    my_label.config(text=input_text)
    
my_button = tkinter.Button(text='Click Me!', command=change_label_text)
my_button.pack()

# Entry == Input
my_input = tkinter.Entry(width=20)
my_input.pack()

# Text
my_text = tkinter.Text(width=30,height=3)
my_text.focus()
my_text.insert("This is demo text")
print(my_text.get("1.0"))
my_text.pack()
windows.mainloop()
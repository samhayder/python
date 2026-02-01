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
my_text.insert(index="1.0", chars="This is demo text")
my_text.pack()

# Spring Box
def use_spring():
    print(my_spring_box.get())
    
my_spring_box = tkinter.Spinbox(from_=0, to=10,width=5,command=use_spring)
my_spring_box.pack()

# Scale
def use_scale(value):
    print(value)
    
my_scale = tkinter.Scale(from_=1,to=100,command=use_scale)
my_scale.pack()

# Check Button
def check_button():
    print(checked_status.get())

checked_status = tkinter.IntVar()
my_check_button = tkinter.Checkbutton(text="Is On?", variable=checked_status,command=check_button)
checked_status.get()
my_check_button.pack()

# Radio Button
def use_radio_button():
    print(radio_state.get())

radio_state = tkinter.IntVar()
my_radio_button1 = tkinter.Radiobutton(text="Radio Button 1", value=1, variable=radio_state,command=use_radio_button)
my_radio_button2 = tkinter.Radiobutton(text="Radio Button 2", value=2, variable=radio_state,command=use_radio_button)
my_radio_button1.pack()
my_radio_button2.pack()

# List Box
def use_list_box(event):
    print(my_list_box.get(my_list_box.curselection()))
    
my_list_box = tkinter.Listbox(height=5)
names = ["Samsddin", "Yasin", "Salman", "Jannat", "Bable"]

for name in names:
    my_list_box.insert(names.index(name),name)
my_list_box.bind("<<ListboxSelect>>",use_list_box)
my_list_box.pack()







windows.mainloop()
import tkinter

def calculate_convert():
    user_value = float(user_input.get())
    km = 1.609
    mile = 0.621
    choose_option = option_status.get()
    converted_result = 0
    
    if user_value <= 0:
        result.config(text="Invalid inputted.")
    elif choose_option == 1:
        converted_result = user_value * mile
        result.config(text=f"{user_value} Km = {round(converted_result,2)} Miles")
    elif choose_option == 2:
        converted_result = user_value * km
        result.config(text=f"{user_value} Mils = {round(converted_result,2)} Kw")
   
        
display = tkinter.Tk()
display.title(string="Distance Convert")
display.minsize(width=300,height=250)
display.config(padx=25,pady=15)


title = tkinter.Label(text="Distance Converter", font=('Arial', 16, 'bold'))
title.grid(row=0, column=1)
title.config(pady=15)

user_input = tkinter.Entry(display, width=8)
user_input.grid(row=2, column=0)

option_text = tkinter.Label(text="Choose an option.")
option_text.grid(row=1, column=1)

option_status = tkinter.IntVar()
option_km = tkinter.Radiobutton(text="Km", value=1, variable=option_status)
option_mils = tkinter.Radiobutton(text="Mils", value=2, variable=option_status)
option_km.grid(row=2 , column=1)
option_mils.grid(row=2, column=2)

result = tkinter.Label(text="", font=('Arial', 18, 'bold'))
result.grid(row=3, column=1)
result.config(pady=15)

calculate_btn = tkinter.Button(text="Calculate", command=calculate_convert)
calculate_btn.grid(row=4, column=1)
calculate_btn.config(padx=12,pady=7)


display.mainloop()
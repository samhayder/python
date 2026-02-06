import tkinter
import tkinter.messagebox
import random
import pyperclip

# --------- ---------- #
def add_data():
    webpage = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if len(webpage) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty.")
    else:
        is_save = tkinter.messagebox.askokcancel(title=webpage, message=f"These are the details\nEmail: {email}\nPassword: {password}\nIs it ok to Save.")
        
        if is_save:
            with open(r"0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.txt",'a') as file:
                file.write(f"{webpage}, {email}, {password}\n")
                tkinter.messagebox.showinfo(title="Save Data", message="Successfully Save Data")
                website_input.delete(0,tkinter.END)
                password_input.delete(0,tkinter.END)
        
# --------- ---------- #
def password_generator():
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+,<>?{}[]|~`"
    
    alpha_pass = [random.choice(alphabets) for _ in range(7) ]
    nums_pass = [random.choice(numbers) for _ in range(4) ]
    sym_pass = [random.choice(symbols) for _ in range(4) ]
    password_list = alpha_pass + nums_pass + sym_pass
    random.shuffle(password_list)
    
    password = "".join(password_list)
    
    password_input.delete(0,tkinter.END)
    password_input.insert(0,password)
    pyperclip.copy(password)
# --------- ---------- #

# ----- UI
display = tkinter.Tk()
display.title("Password Manager")
display.config(padx=50,pady=50)

# ----- Canvas
canvas = tkinter.Canvas(width=250,height=250,highlightthickness=0)
pass_image = tkinter.PhotoImage(file="0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/pass.png")
canvas_image = canvas.create_image(125,125,image=pass_image)
canvas.grid(row=0,column=1)

# ----- Label
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3,column=0)


# ----- Entry
website_input = tkinter.Entry(width=52)
website_input.grid(row=1,column=1, columnspan=2)
website_input.focus()
email_input = tkinter.Entry(width=52)
email_input.grid(row=2,column=1, columnspan=2)
email_input.insert(0,"sams.seul@gamil.com")
password_input = tkinter.Entry(width=34)
password_input.grid(row=3,column=1)

# ----- Button
password_generate_btn = tkinter.Button(text="Generate Password", command=password_generator)
password_generate_btn.grid(row=3,column=2)
add_btn = tkinter.Button(text="Add",width=35, command=add_data)
add_btn.config(padx=30,pady=0)
add_btn.grid(row=4,column=1,columnspan=2)



display.mainloop()
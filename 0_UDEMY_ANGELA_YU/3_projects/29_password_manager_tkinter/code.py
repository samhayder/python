import tkinter
import tkinter.messagebox
import random
import pandas

# ---------- Constant Variable ---------- #

# ---------- Password Generator Function ---------- #
def password_generator():
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+,<>?{}[]|~`"
    
    password = ""
    
    for i in range(20):
        if i % 2 == 0:
            password += random.choice(alphabets)
        elif i % 3 == 0:
            password += random.choice(symbols)
        else:
            password += random.choice(numbers)
    password_input.delete(0, tkinter.END)
    password_input.insert(0,password)
    
# ---------- Add Whole Data function ---------- #
def add_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if website == "":
        tkinter.messagebox.showinfo("Website","Website input value empty")
        exit()
        
    
    data = {
        "Website" : [website],
        "Email" : [email],
        "Password" : [password]
    }
    
    df = pandas.DataFrame.from_dict(data)
    df.to_csv("0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.csv", index=False)
    print(df)
    
# ---------- ---------- #
# ---------- ---------- #

# ----- UI
display = tkinter.Tk()
# display.minsize(width=300,height=250)
display.title("Password Manager")
display.config(padx=50,pady=50)

# ----- Canvas
canvas = tkinter.Canvas(width=250,height=250,highlightthickness=0)
pass_image = tkinter.PhotoImage(file="0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/pass.png")
canvas_image = canvas.create_image(125,125,image=pass_image)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1,column=0)
website_input = tkinter.Entry(width=52)
website_input.grid(row=1,column=1, columnspan=2)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2,column=0)
email_input = tkinter.Entry(width=52)
email_input.grid(row=2,column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3,column=0)
password_input = tkinter.Entry(width=34)
password_input.grid(row=3,column=1)

password_generate_btn = tkinter.Button(text="Generate Password", command=password_generator)
password_generate_btn.grid(row=3,column=2)

add_btn = tkinter.Button(text="Add",width=35, command=add_data)
add_btn.config(padx=30,pady=0)
add_btn.grid(row=4,column=1,columnspan=2)



display.mainloop()
import tkinter
import tkinter.messagebox
import random
import pyperclip
import json

# --------- Save Data with JSON mode function ---------- #
# Read => json.load() - Reading old data == 'r' mode
# Update => json.update() - Updating old data with new data
# Write => json.dump() - Saving updated data == 'w'
def save_data_with_json():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "Email": email,
            "Password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="OPPs!", message="Please make sure you haven't left any fields empty.")
    
    else:
        is_save = tkinter.messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nAre you save this data?")
        if is_save:
            try:
                with open("0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.json",'r') as file:
                    data = json.load(file)
            except:
                with open("0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.json",'w') as file:
                    json.dump(new_data,file,indent=4) 
            else:
                data.update(new_data)
                
                with open("0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.json",'w') as file:
                    json.dump(data,file,indent=4)
                                    
            finally:
                website_input.delete(0,tkinter.END)
                password_input.delete(0,tkinter.END)
                tkinter.messagebox.showinfo(title="Save Data Info", message=f"Email: {email}\nPassword: {password}\nThis data save successfully.")
            
        

# --------- Save Data with txt mode function ---------- #
def save_data_with_txt():
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
        
# --------- Search Data Function ---------- #
def search_btn():
    website = website_input.get().strip().title()
    
    try:
        with open("0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
            tkinter.messagebox.showinfo(title="OOPs!", message="No Data file found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            tkinter.messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            tkinter.messagebox.showinfo(title="OOPs!", message=f"No details for {website} exists.")
   

# --------- Updating Data by Search Function ---------- #
def update_data_by_search():
    website = website_input.get().strip().title()
    
    with open("0_UDEMY_ANGELA_YU/3_projects/29_password_manager_tkinter/data.json") as file:
        data = json.load(file)
        
    if website in data:
        email = data[website]["Email"]
        password = data[website]["Password"]
        # Delete old data
        website_input.delete(0,tkinter.END)
        email_input.delete(0,tkinter.END)
        # Show data to save
        website_input.insert(0, website)
        email_input.insert(0, email)
        password_input.insert(0, password)

# --------- Password Generator Function ---------- #
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
website_input = tkinter.Entry(width=34)
website_input.grid(row=1,column=1)
website_input.focus()
email_input = tkinter.Entry(width=52)
email_input.grid(row=2,column=1, columnspan=2)
email_input.insert(0,"sams.seul@gamil.com")
password_input = tkinter.Entry(width=34)
password_input.grid(row=3,column=1)

# ----- Button
search_btn = tkinter.Button(text="Search",width=15, command=search_btn)
search_btn.grid(row=1,column=2)
password_generate_btn = tkinter.Button(text="Generate Password", command=password_generator)
password_generate_btn.grid(row=3,column=2)
add_btn = tkinter.Button(text="Add",width=35, command=save_data_with_json)
add_btn.config(padx=30,pady=0)
add_btn.grid(row=4,column=1,columnspan=2)



display.mainloop()
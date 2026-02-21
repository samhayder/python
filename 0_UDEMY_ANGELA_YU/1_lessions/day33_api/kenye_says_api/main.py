import tkinter
import requests


# Get Quote API
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    
    data = response.json()
    quote = data['quote']
    canvas.itemconfig(quote_text, text=f"{quote}")


display = tkinter.Tk()
display.title(string="Kenye Says...")
display.config(padx=50,pady=50)

# Canvas
canvas = tkinter.Canvas(width=300, height=414, highlightthickness=0)
bg_img = tkinter.PhotoImage(file="0_UDEMY_ANGELA_YU/1_lessions/day33_api/kenye_says_api/img/background.png")
create_bg_img = canvas.create_image(150,206,image=bg_img)
quote_text = canvas.create_text(150,207, text="", fill="#fff", font=('Arial',16,'bold'), width=250)
canvas.grid(row=0,column=0)

# Button
btn_img = tkinter.PhotoImage(file="0_UDEMY_ANGELA_YU/1_lessions/day33_api/kenye_says_api/img/kanye.png")
quote_btn = tkinter.Button(image=btn_img, highlightthickness=1, command=get_quote)
quote_btn.grid(row=1,column=0)




display.mainloop()
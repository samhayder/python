import tkinter
import pandas
import random

# ----- Constant Variable ---- #
BACKGROUND_COLOR = "#98A8A0"
FRONT_IMG = "0_UDEMY_ANGELA_YU/3_projects/31_flash_card_capstone_project/images/card_front.png"
BACK_IMG = "0_UDEMY_ANGELA_YU/3_projects/31_flash_card_capstone_project/images/card_back.png"
KNOWN_BTN = "0_UDEMY_ANGELA_YU/3_projects/31_flash_card_capstone_project/images/right.png"
UNKNOWN_BTN = "0_UDEMY_ANGELA_YU/3_projects/31_flash_card_capstone_project/images/wrong.png"
FR_CSV_FILE = "0_UDEMY_ANGELA_YU/3_projects/31_flash_card_capstone_project/data/french_words.csv"
LEARN_WORD_CSV = "0_UDEMY_ANGELA_YU/3_projects/31_flash_card_capstone_project/data/learn_words.csv"
data_dict = {}
current_word = {}

# ---------- Get CSV Data file --------- #
try:
    data = pandas.read_csv(LEARN_WORD_CSV)
except FileNotFoundError:
    original_data = pandas.read_csv(FR_CSV_FILE)
    data_dict = original_data.to_dict(orient='records')
else:
    # data_dict = {row.French:row.English for (index,row) in data.iterrows()}
    data_dict = data.to_dict(orient='records')

# ---------- Pick a Random Word  --------- #
def next_card():
    global current_word, flip_timing
    display.after_cancel(flip_timing)
    
    current_word = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French", fill="#000")
    canvas.itemconfig(card_word, text=current_word["French"], fill="#000")
    canvas.itemconfig(create_card_img, image=card_front_img)
    
    flip_timing = display.after(ms=3000, func=flip_card)

# ---------- Known Word function --------- #
def is_known():
    data_dict.remove(current_word)
    data = pandas.DataFrame(data_dict)
    data.to_csv(LEARN_WORD_CSV, index=False)
    next_card()
    
# ---------- Flip Card function --------- #
def flip_card():
    canvas.itemconfig(title_text, text="English", fill="#fff")
    canvas.itemconfig(card_word, text=current_word["English"], fill="#fff")
    canvas.itemconfig(create_card_img, image=card_back_img)
# ----------  --------- #

# ----- Setup UI ---- #
display = tkinter.Tk()
display.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timing = display.after(ms=3000, func=flip_card)
# ----- Canvas of front img ---- #
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = tkinter.PhotoImage(file=FRONT_IMG)
card_back_img = tkinter.PhotoImage(file=BACK_IMG)
create_card_img = canvas.create_image(400,263,image=card_front_img)
title_text = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0, columnspan=2)

# ----- Unknown btn img ---- #
unknown_btn_img = tkinter.PhotoImage(file=UNKNOWN_BTN)
unknown_btn = tkinter.Button(image=unknown_btn_img, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1,column=0)
# ----- Known btn img ---- #
known_img = tkinter.PhotoImage(file=KNOWN_BTN)
known_btn = tkinter.Button(image=known_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)
# -----  ---- #
next_card()

display.mainloop()

# -----  ---- #
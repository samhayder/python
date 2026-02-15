import tkinter
import math

# ---------- Constant Variable
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
count_data = 0
timer = None

# ---------- Show Start Function ---------- #
def start_timer():
    global count_data,check_marks
    count_data += 1
    minimum_work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if count_data == 8:
        count_down(long_break)
        title.config(text="Break", fg=RED,bg=YELLOW)
    elif count_data % 2 == 0:
        count_down(short_break)
        title.config(text="Break",fg=PINK,bg=YELLOW)
    else:
        count_down(minimum_work)
        title.config(text="Working",fg=GREEN,bg=YELLOW)

# ---------- Time Count Down Timer ---------- #
def count_down(count):
    global timer
    minute = math.floor(count / 60)
    second = count % 60
    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{count}"
        
    canvas.itemconfig(canvas_text, text=f"{minute}:{second}")
    
    if count > 0:
        timer = display.after(1000,count_down,count-1)
    else:
        start_timer()
        session = math.floor(count_data/2)
        marks = ""
        
        for _ in range(session):
            marks += "✔"
        check_mark.config(text=marks)
        
# ---------- Reset Function ---------- #
def reset_btn():
    global count_data
    display.after_cancel(timer)
    count_data = 0
    canvas.itemconfig(canvas_text,text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")

# ---------- Show Display by tkinter
display = tkinter.Tk()
display.title(string="Count Down Project")
display.config(padx=100,pady=75,bg=YELLOW)

# ---------- Show Label of Title
title = tkinter.Label(text="Timer", font=(FONT_NAME,36,'bold'), fg=GREEN,bg=YELLOW)
title.grid(row=0, column=1)

# ---------- Show Canvas by tkinter
canvas = tkinter.Canvas(width=220,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="0_UDEMY_ANGELA_YU/3_projects/28_pomodor_tkinter/tomato.png")
canvas_image = canvas.create_image(110,112,image= tomato_img)
canvas_text = canvas.create_text(110,130, text="00:00", font=(FONT_NAME,36,'bold'),fill="White")
canvas.grid(row=1, column=1)

# ---------- Show Start Button
start_btn = tkinter.Button(text="Start",highlightthickness=0, font=(FONT_NAME,10,'bold'), command=start_timer)
start_btn.config(padx=8,pady=4)
start_btn.grid(row=2, column=0)

# ---------- Show Reset Button
reset_btn = tkinter.Button(text="Reset", highlightthickness=0, font=(FONT_NAME,10,'bold'), command=reset_btn)
reset_btn.config(padx=8,pady=4)
reset_btn.grid(row=2, column=3)

# ---------- Show Check Mark
check_mark = tkinter.Label(text="", font=(FONT_NAME,16), fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)




display.mainloop()
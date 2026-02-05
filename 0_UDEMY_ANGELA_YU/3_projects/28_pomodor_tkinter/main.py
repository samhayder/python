import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_minute =  WORK_MIN * 60
    short_break_minute = SHORT_BREAK_MIN * 60
    long_break_minute = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_minute)
        title.config(text="Long Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break_minute)
        title.config(text="Short Break", fg=GREEN)
    else:
        count_down(work_minute)
        title.config(text="Work", fg=PINK)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    
    if count_second < 10:
        count_second = f"0{count_second}"
    
    canvas.itemconfig(canvas_text,text=f"{count_minute}:{count_second}")
    if count > 0:
        display.after(1000,count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
display = tkinter.Tk()
display.title(string="Pomodoro Project")
display.config(padx=100,pady=50,bg=YELLOW)

title = tkinter.Label(text="Timer", font=(FONT_NAME,24,'bold'), fg=GREEN,bg=YELLOW)
title.grid(row=0, column=1)
# --- Image of tomato
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='0_UDEMY_ANGELA_YU/3_projects/28_pomodor_tkinter/tomato.png')
canvas_create_img = canvas.create_image(100,112,image=tomato_img)
canvas_text = canvas.create_text(100,130, text="00:00", fill="White", font=(FONT_NAME,36, 'bold'))
canvas.grid(row=1, column=1)

start_btn = tkinter.Button(text="Start",command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = tkinter.Button(text="Reset")
reset_btn.grid(row=2, column=2)

check_mark = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)






display.mainloop()





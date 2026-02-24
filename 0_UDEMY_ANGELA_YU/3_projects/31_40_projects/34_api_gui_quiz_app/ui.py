from tkinter import *
from quiz import Quiz

BG_COLOR = "#2B3F4B"

class QuizInterface:
    def __init__(self, quiz:Quiz):
        self.quiz = quiz
        
        self.window = Tk()
        self.window.title(string="Quiz App")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)
        
        self.score = Label(text="Score: 0", bg=BG_COLOR, fg="#fff")
        self.score.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=200, bg="#fff")
        self.quiz_text = self.canvas.create_text(150,100, width=280, text="Some quiz text", font=('Arial', 18, 'italic'), fill=BG_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.false_img = PhotoImage(file="0_UDEMY_ANGELA_YU/3_projects/31_40_projects/34_api_gui_quiz_app/images/false.png")
        self.true_img = PhotoImage(file="0_UDEMY_ANGELA_YU/3_projects/31_40_projects/34_api_gui_quiz_app/images/true.png")
        
        self.false_btn = Button(image=self.false_img, command=self.false_btn_pressed)
        self.false_btn.grid(row=2, column=0)
        
        self.true_btn = Button(image=self.true_img, command=self.true_btn_pressed)
        self.true_btn.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="#fff")
        if self.quiz.still_has_question():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text=f"You've reached end of the quiz.\n Your Current Score {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
        
    def false_btn_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)
    
    def true_btn_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)
        
    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(ms=1000, func=self.get_next_question)
            
            
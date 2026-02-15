from data import question_data

class Question:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
        
question_lists = []
for item in question_data:
    item_question = item['question']
    item_answer = item['correct_answer']
    next_question = Question(item_question,item_answer)
    question_lists.append(next_question)
    

print(question_lists)
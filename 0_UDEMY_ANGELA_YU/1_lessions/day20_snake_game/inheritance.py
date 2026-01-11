class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breath(self):
        print("Inhaler in breath.")
        

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def swim(self):
        print("Swim is underwater.")

hilsha = Fish()

hilsha.breath()
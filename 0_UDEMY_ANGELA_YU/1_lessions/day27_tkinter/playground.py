def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(f"Total= {sum}")
        
# add(2,3,10,52,12,65)

def calculate(**kwargs):
    n = 0
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
    
    
# print(calculate(add=3, multiply=5))


class Calc:
    def __init__(self,**kwargs):
        self.add = kwargs.get('add')
        self.subtract = kwargs.get('subtract')
        self.multiply = kwargs.get('multiply')
        self.division = kwargs.get('division')
        
        
sum_calc = Calc(add=5,subtract=3)
sum_calc.do_cal(a=2,b=4)
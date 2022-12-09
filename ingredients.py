from return_integer import get_int

#define a ingredient:
class Ingredient:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def get_ingredient_count(self):    
        return self.count

    def set_ingredient_count(self, new_count):
        new_count = get_int()    
        self.count = new_count       

banana = Ingredient("banana", 1)               

print(banana.get_ingredient_count())
banana.set_ingredient_count("a")
print(banana.get_ingredient_count())

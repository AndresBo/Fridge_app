import csv

def list_foods():
    with open('food_list.csv') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"{row[0]}, {row[1]}")


          


# #define a ingredient:
# class Ingredient:
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count

#     def get_ingredient_count(self):    
#         return self.count

#     def set_new_ingredient(self):
#         while True:
#             self.name = input("name of new ingredient?").lower().strip()
#             if self.name in ingredients_list:
#                 print("This ingredient is already in the fridge, please enter again")
#                 continue
#             break
#         print("How much of the ingredient do we have?")
#         self.count = get_int
        
#         ingredients_list[self.name] = self.count

#         print(f"{self.count} of {self.name} has been added to the fridge")

#     def set_ingredient_count(self, new_count):
#         new_count = get_int()    
#         self.count = new_count       

# banana = Ingredient("banana", 1)               

# print(banana.get_ingredient_count())
# banana.set_ingredient_count("a")
# print(banana.get_ingredient_count())

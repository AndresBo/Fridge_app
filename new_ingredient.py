import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from return_integer import get_int

def ask_new_food():
    new_food = get_string()            
    set_food_in_list = build_set_name()
    quantity = 0
    new_food_list = []

    if new_food in set_food_in_list:
        print(f"{new_food} is already in Fridge")
    else:
        quantity = get_int() 
        new_food_list.append(new_food)
        new_food_list.append(quantity)
        add_new_ingredient(new_food_list)
        print(f"{quantity} {new_food} have been added")



# add new row to csv file from new_food list
def add_new_ingredient(new):
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new)
        f.close()

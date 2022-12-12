import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name

def ask_new_food():
    new_food = get_string()
    set_food_in_list = build_set_name()

    if new_food in set_food_in_list:
        print(f"{new_food} is already in Fridge")
    else:
        print(f"{new_food} is not in {set_food_in_list}")



# add new row to csv file from new_food list
def add_new_ingredient():
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_food)
        f.close()

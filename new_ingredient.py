import csv
from return_lower_case_string import get_string

def ask_new_food():
    new_food_name = get_string()
    

new_food = []

# add new row to csv file from new_food list
def add_new_ingredient():
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_food)
        f.close()
print(ask_new_food())

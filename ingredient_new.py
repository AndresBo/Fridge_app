import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from return_integer import get_int

def ask_new_food():
    new_food = get_string()             #use get_string function to get new food name from user
    if new_food is None:                #option to get back to start menu
        return

    set_food_in_list = build_set_name() #get a set with current foods
    quantity = 0                        #create variable to hold quantity of new food
    new_food_list = []                  #create list to hold name and quatity of new food 

    if new_food in set_food_in_list:   
        print(f"{new_food} is already in Fridge")
    else:
        quantity = get_int()           #get new food quantity using get_int function 
        new_food_list.append(new_food) 
        new_food_list.append(quantity)
        add_new_ingredient(new_food_list)
        print(f"{quantity} {new_food} have been added") #call add_new_ingredient passing list [name,quantity]



# add new row to csv file from new_food list
def add_new_ingredient(newList):
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newList)
        f.close()

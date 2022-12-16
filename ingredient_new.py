import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from return_integer import get_int

food_list = 'food_list.csv'

# Asks for new food item:
def ask_new_food():
    print("Enter new food")
    #Use get_string function to get new food name from user
    new_food = get_string()
    #Option to get back to start menu if get_string returns None             
    if new_food is None:                
        return
    #Get a set with current foods from build_set_name function
    set_food_in_list = build_set_name(food_list) 
    quantity = 0                                 
    new_food_list = []                           
    #Checks if new_food is in set of current food
    if new_food in set_food_in_list:     
        print(f"{new_food} is already in Fridge")    
    else:
        quantity = get_int()              #get new food quantity using get_int function 
        new_food_list.append(new_food)    #add new food name to new_food_list
        new_food_list.append(quantity)    #add new food quantity to new_food_list
        add_new_ingredient(new_food_list) #calls function add_new_ingredients located a few lines below   
        print(f"{quantity} {new_food} have been added") #print confirmation                              
                                                                                                        

# Add new row to csv file from new_food list using csv module:
def add_new_ingredient(newList):
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newList)
        f.close()

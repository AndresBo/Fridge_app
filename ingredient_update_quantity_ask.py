from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from return_integer import get_int
from ingredient_update_quantity import update_food_quantity
food_list = 'food_list.csv'

def update_food_ask():
    print("Update food quantity")            
    food_to_update = get_string()             #get food name user wishes to updated
    if food_to_update is None:                #option to get back to start menu
        return
    
    set_food_in_list = build_set_name(food_list)  #get set of current food 
    
    if food_to_update in set_food_in_list:   #if food in the set of current food:
        new_quantity = get_int()             #get new quantity
 
        updated_food = list()                #build new list
    
        updated_food.append(food_to_update)
        updated_food.append(new_quantity)
    
        update_food_quantity(updated_food)   #call update_food_quantity function 

        print(f"quantity of {food_to_update} has been updated to {new_quantity}")
    else:
        print(f"{food_to_update} is not in the list")

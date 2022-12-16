from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from return_integer import get_int
from ingredient_update_quantity import update_food_quantity

food_list = 'food_list.csv'

def update_food_ask():
    
    print("\nUpdate food quantity")
    # Get food name user wishes to updated            
    food_to_update = get_string() 
    # Option to get back to start menu            
    if food_to_update is None:                
        return
    # Get set of current food 
    set_food_in_list = build_set_name(food_list)  
    # If food in the set of current food:  
    if food_to_update in set_food_in_list:   
        # Get new quantity
        new_quantity = get_int()             
        # Build list with updated quantity
        updated_food = list()                
        updated_food.append(food_to_update)
        updated_food.append(new_quantity)
        # Call update_food_quantity function 
        update_food_quantity(updated_food)   
        # Print confirmation
        print(f"quantity of {food_to_update} has been updated to {new_quantity}")
    else:
        # Print not in the list
        print(f"{food_to_update} is not in the list")

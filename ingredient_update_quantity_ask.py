from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from return_integer import get_int
from ingredient_update_quantity import update_food_quantity


def update_food_ask():
    food_to_update = get_string()
    if food_to_update is None:                #option to get back to start menu
        return
    
    set_food_in_list = build_set_name()
    
    if food_to_update in set_food_in_list:
        new_quantity = get_int()

        updated_food = list()
    
        updated_food.append(food_to_update)
        updated_food.append(new_quantity)
    
        update_food_quantity(updated_food)

        print(f"quantity of {food_to_update} has been updated to {new_quantity}")
    else:
        print(f"{food_to_update} is not in the list")

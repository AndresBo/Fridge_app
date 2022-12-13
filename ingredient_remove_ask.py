import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from ingredient_remove import remove_food
# https://stackoverflow.com/questions/56987312/how-to-delete-only-one-row-in-csv-with-python
def remove_food_ask():
    print("Remove food")
    food_to_remove = get_string()
    if food_to_remove is None:                #option to get back to start menu
        return
        
    set_of_food_in_list = build_set_name()

    if food_to_remove in set_of_food_in_list:
        remove_food(food_to_remove)
        print(f"{food_to_remove} has been deleted")
    else:
        print(f"{food_to_remove} is not in the list") 

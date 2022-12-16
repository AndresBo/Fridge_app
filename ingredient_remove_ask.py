import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name
from ingredient_remove import remove_food

food_list = 'food_list.csv' 

# Function that: Lists current food, 
#                Gets name of food to remove, 
#                Gets set of current food,
#                Compares name of food to remove against set of current food
def remove_food_ask():
    print("Remove food")
    food_to_remove = get_string()
    #Option to get back to start menu
    if food_to_remove is None:                
        return
    #Gets set of current food    
    set_of_food_in_list = build_set_name(food_list)    
    #Compares if food is in set or not, if TRUE delete, if FALSE notify user.
    if food_to_remove in set_of_food_in_list: 
        remove_food(food_to_remove)                  #calls remove_food function
        print(f"{food_to_remove} has been deleted")  #prints confirmation
    else:
        print(f"{food_to_remove} is not in the list") #print food is not in current set of foods.

from os import system
from ingredients_list import list_foods
list = 'food_list.csv'
# get a LOWER case string with leading and trailing whitespace removed
def get_string():
    while True:
        print("\n")
        list_foods(list)
        
        food_name = input("\nPlease enter name of food or to head back to menu enter 'back': ").lower().strip()
        if food_name == "back":
            break
        elif not food_name.isalpha():
            system('clear')
            print("Enter only letters")
            input("\nPress enter to continue")
            system('clear')
            continue
        else:
            return food_name
            break

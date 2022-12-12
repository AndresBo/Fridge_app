from os import system
from welcome_date import welcome_date
from ingredients_list import list_foods
from ingredient_new import ask_new_food
from ingredient_remove_ask import remove_food_ask

def start_menu():
    print("\n------------ Welcome to FRIDGE ------------")
    print(welcome_date())
    print("\nPlease select from the following options by entering the number:")
    print("1. List foods in fridge")
    print("2. Enter new food")
    print("3. Remove food")
    print("4. Update food quantity")
    print("5. Exit")
    selection = input("\nPlease enter your selection: ")
    return selection
    
selection = ""
while selection != "5":
    system('clear')
    selection = start_menu()
    system('clear')
    if selection == "1": # list foods
        list_foods()
    elif selection == "2": # enter new food
        ask_new_food()
    elif selection == "3": # remove food
        remove_food_ask()
    elif selection == "4": # query food amount
        print("query food")
    elif selection == "5": #exit
        continue
    else:
        print("Invalid input")
    input("\nPress enter to continue")
    system('clear')

print("bye")

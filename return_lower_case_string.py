from os import system
# get a lower case string with leading and trailing whitespace removed
def get_string():
    while True:
        
        new_food = input("Please enter name of new food or to head back to menu enter 'back': ").lower().strip()
        if new_food == "back":
            break
        elif not new_food.isalpha():
            system('clear')
            print("Enter only letters")
            input("\nPress enter to continue")
            continue
        else:
            return new_food
            break
#print(get_string()) 

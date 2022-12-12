from os import system
# get a LOWER case string with leading and trailing whitespace removed
def get_string():
    while True:
        
        food_name = input("Please enter name of food or to head back to menu enter 'back': ").lower().strip()
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

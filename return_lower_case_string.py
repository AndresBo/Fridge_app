# get a lower case string with leading and trailing whitespace removed
def get_string():
    while True:
        new_food = input("Please enter name of new food: ").lower().strip()

        if not new_food.isalpha():
            print("Enter only letters")
            continue
        else:
            return new_food
            break
    

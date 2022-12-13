import csv
food_list = 'food_list.csv'
# list of food function using csv module:
def list_foods():
    with open(food_list) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print (f"{row['food']} {row['quantity']}")
            

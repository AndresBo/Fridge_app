import csv

# list of food function using csv module:
def list_foods():
    with open('food_list.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print (f"{row['food']} {row['quantity']}")
            

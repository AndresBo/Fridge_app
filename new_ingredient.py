import csv

new_food = []

# def enter_ingredient():
def add_new_ingredient(new_food):
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_food)
        f.close()
